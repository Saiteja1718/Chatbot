"""
Lightweight rule-based chatbot for diet and nutrition questions.

This version is designed to run reliably on Streamlit Cloud without
loading large LLM models (no torch/transformers required).
"""

from __future__ import annotations

import textwrap
from typing import List


def _summarize_context(context_text: str, max_items: int = 5) -> List[str]:
    """Extract a few recipe lines from the context to mention in answers."""
    lines = [ln.strip() for ln in context_text.splitlines() if ln.strip()]
    # Heuristic: only keep lines that look like recipe bullets or names
    candidates = [
        ln for ln in lines if "-" in ln or "Calories" in ln or "kcal" in ln
    ]
    return candidates[:max_items]


def generate_chat_answer(context_text: str, history_text: str, user_message: str) -> str:
    """
    Generate a simple, helpful text answer without using a heavy LLM.

    Args:
        context_text: Text describing current recommended recipes and ingredients.
        history_text: Previous turns in the conversation (not deeply parsed here).
        user_message: The latest user question.
    """
    question = user_message.strip()
    q_lower = question.lower()

    # Extract a few context snippets to ground the answer
    context_snippets = _summarize_context(context_text)

    # Simple intent detection
    if any(word in q_lower for word in ["swap", "substitute", "instead of", "alternative"]):
        base = (
            "You can usually substitute within the same ingredient family. "
            "For example, swap similar proteins (chicken ↔ turkey ↔ tofu), "
            "starches (rice ↔ quinoa ↔ pasta), or veggies with similar texture. "
        )
    elif any(word in q_lower for word in ["protein", "high protein", "more protein"]):
        base = (
            "To increase protein, emphasize dishes with lean meats, fish, eggs, "
            "Greek yogurt, beans, or lentils. You can also slightly increase the "
            "portion size of the protein in each meal while keeping fats and "
            "added sugars moderate. "
        )
    elif any(word in q_lower for word in ["calorie", "kcal", "lose weight", "deficit"]):
        base = (
            "To reduce calories, keep the same meal structure but trim oils, "
            "creamy sauces, sugary drinks, and large starchy portions. "
            "Fill more of the plate with vegetables and lean protein. "
        )
    elif any(word in q_lower for word in ["budget", "cheap", "affordable", "low cost"]):
        base = (
            "To keep meals budget‑friendly, focus on pantry staples like beans, "
            "lentils, eggs, frozen vegetables, oats, and rice. Choose recipes "
            "with fewer specialty ingredients and re‑use the same items across "
            "multiple days. "
        )
    else:
        base = (
            "Here are some general guidelines based on your current meal plan. "
            "Aim for balanced plates with lean protein, whole‑grain or starchy "
            "carbs, plenty of vegetables, and moderate healthy fats. Adjust "
            "portion sizes to match your calorie and protein goals. "
        )

    if context_snippets:
        base += "From your current plan, a few example items are:\n"
        for snip in context_snippets:
            base += f"- {snip}\n"

    base += (
        "\nUse these as templates: keep the structure of the meal but swap "
        "ingredients within the same category (protein, carb, veggie, fat) "
        "to match your tastes, allergies, or budget."
    )

    return textwrap.fill(base, width=90)


def clear_model_cache() -> None:
    """
    Kept for API compatibility with the previous implementation.
    Nothing to clear because we no longer hold a large model in memory.
    """
    return None
