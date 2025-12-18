"""
Local LLM-based chatbot for diet and nutrition questions.
Uses TinyLlama model running locally via Hugging Face transformers.
No API keys required.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings

warnings.filterwarnings("ignore")

# Global variables to cache the model and tokenizer
_model = None
_tokenizer = None
_device = None

def load_model():
    """
    Lazily load the TinyLlama model and tokenizer.
    Loads only once and caches for subsequent calls.
    """
    global _model, _tokenizer, _device
    
    if _model is not None and _tokenizer is not None:
        return _model, _tokenizer, _device
    
    print("Loading TinyLlama model... This may take a moment on first run.")
    
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    
    # Determine device
    _device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {_device}")
    
    # Load tokenizer
    _tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Set pad token to eos token if not set
    if _tokenizer.pad_token is None:
        _tokenizer.pad_token = _tokenizer.eos_token
    
    # Load model
    _model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if _device == "cuda" else torch.float32,
        device_map="auto" if _device == "cuda" else None,
        low_cpu_mem_usage=True
    )
    
    if _device == "cpu":
        _model = _model.to(_device)
    
    _model.eval()
    
    print("Model loaded successfully!")
    
    return _model, _tokenizer, _device


def generate_chat_answer(context_text: str, history_text: str, user_message: str) -> str:
    """
    Generate a chat response using the local LLM.
    
    Args:
        context_text: Text describing current recommended recipes and ingredients
        history_text: Compact text representation of previous chat turns
        user_message: The latest user question
        
    Returns:
        The assistant's reply as a string
    """
    try:
        model, tokenizer, device = load_model()
        
        # Build the prompt using TinyLlama's chat format
        system_prompt = """You are a helpful diet and nutrition assistant. You answer questions about recommended recipes, ingredients, substitutions, and simple modifications. Keep your answers concise and practical. If a question is unrelated to food or nutrition, politely say you don't know."""
        
        # Format the prompt
        prompt = f"""<|system|>
{system_prompt}

Current Recommendations:
{context_text}
</s>
"""
        
        # Add conversation history if available
        if history_text.strip():
            # Parse history to extract only recent exchanges (last 3 to keep context manageable)
            history_lines = history_text.strip().split('\n')
            recent_history = history_lines[-6:] if len(history_lines) > 6 else history_lines
            
            for line in recent_history[:-1]:  # Exclude the current user message (it's already in user_message)
                if line.startswith("User:"):
                    prompt += f"<|user|>\n{line[5:].strip()}</s>\n"
                elif line.startswith("Assistant:"):
                    prompt += f"<|assistant|>\n{line[10:].strip()}</s>\n"
        
        # Add current user message
        prompt += f"<|user|>\n{user_message}</s>\n<|assistant|>\n"
        
        # Tokenize
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1536)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        # Generate
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
                repetition_penalty=1.1
            )
        
        # Decode the generated tokens (excluding the prompt)
        generated_tokens = outputs[0][inputs['input_ids'].shape[1]:]
        response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
        
        # Clean up the response
        response = response.strip()
        
        # Remove any accidental repetition of the user's question
        if response.startswith(user_message):
            response = response[len(user_message):].strip()
        
        return response if response else "I'm not sure how to answer that. Could you rephrase your question?"
        
    except Exception as e:
        print(f"Error generating chat response: {e}")
        return f"Sorry, I encountered an error: {str(e)}. Please try again."


def clear_model_cache():
    """
    Clear the model from memory to free up resources.
    Call this if you need to release memory.
    """
    global _model, _tokenizer, _device
    
    if _model is not None:
        del _model
        _model = None
    
    if _tokenizer is not None:
        del _tokenizer
        _tokenizer = None
    
    _device = None
    
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    print("Model cache cleared.")
