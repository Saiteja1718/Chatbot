import numpy as np
import re
import pandas as pd
import streamlit as st
import os


# Heuristic filters to drop clearly non-food / noisy recipe names that slip
# through from the original dataset (e.g. maintenance-related terms).
UNWANTED_NAME_KEYWORDS = [
    "clean out",
    "cleanout",
    "clean-out",
    "hot sauce",
]


def _filter_valid_recipes(df: pd.DataFrame) -> pd.DataFrame:
    if "Name" not in df.columns:
        return df

    mask = pd.Series(True, index=df.index)
    for kw in UNWANTED_NAME_KEYWORDS:
        mask &= ~df["Name"].str.contains(kw, case=False, na=False)
    return df[mask]


# Load dataset once at module level
@st.cache(allow_output_mutation=True)
def load_dataset():
    # Try multiple paths for different deployment scenarios.
    # We now standardize on the enhanced dataset only to keep the repo smaller.
    possible_paths = [
        os.path.join(os.path.dirname(__file__), '..', 'Data', 'dataset_enhanced.csv'),  # Local with cuisine tags
        os.path.join('Data', 'dataset_enhanced.csv'),  # Streamlit Cloud
        'Data/dataset_enhanced.csv',
    ]
    
    for dataset_path in possible_paths:
        if os.path.exists(dataset_path):
            df = pd.read_csv(dataset_path, compression='gzip')
            # Check if Cuisine column exists, if not add it as 'Other'
            if 'Cuisine' not in df.columns:
                df['Cuisine'] = 'Other'
            df = _filter_valid_recipes(df)
            return df
    
    # If none found, raise error
    raise FileNotFoundError("Could not find dataset_enhanced.csv in expected locations")

def extract_data(dataframe, ingredients):
    extracted_data = dataframe.copy()
    extracted_data = extract_ingredient_filtered_data(extracted_data, ingredients)
    return extracted_data


def extract_ingredient_filtered_data(dataframe, ingredients):
    extracted_data = dataframe.copy()
    regex_string = ''.join(map(lambda x: f'(?=.*{x})', ingredients))
    extracted_data = extracted_data[extracted_data['RecipeIngredientParts'].str.contains(
        regex_string, regex=True, flags=re.IGNORECASE)]
    return extracted_data


def recommend(dataframe, _input, ingredients=[], params={'n_neighbors': 5, 'return_distance': False}):
    """
    Pure NumPy implementation of the original scikit-learn pipeline:
    - Standardize numeric nutrition columns
    - Compute cosine similarity to the query vector
    - Return top-k most similar recipes
    """
    extracted_data = extract_data(dataframe, ingredients)
    k = params.get('n_neighbors', 5)

    if extracted_data.shape[0] < k:
        return None

    # Numeric nutrition features are columns 6:15 in the original dataset
    features = extracted_data.iloc[:, 6:15].to_numpy(dtype=float)

    # Standardize (equivalent to StandardScaler)
    mean = features.mean(axis=0)
    std = features.std(axis=0)
    std[std == 0] = 1.0
    features_std = (features - mean) / std

    # Standardize input
    x = np.array(_input, dtype=float).reshape(1, -1)
    x_std = (x - mean) / std

    # Cosine similarity
    x_norm = np.linalg.norm(x_std, axis=1, keepdims=True)  # (1, 1)
    X_norm = np.linalg.norm(features_std, axis=1, keepdims=True)  # (n, 1)
    sim = (features_std @ x_std.T) / (X_norm * x_norm + 1e-12)  # (n, 1)

    # Take top-k highest similarity
    top_k_idx = np.argsort(-sim[:, 0])[:k]
    return extracted_data.iloc[top_k_idx]


def extract_quoted_strings(s):
    strings = re.findall(r'"([^"]*)"', s)
    return strings


def output_recommended_recipes(dataframe):
    if dataframe is not None:
        output_df = dataframe.copy()
        # Apply the same name filter to be extra safe even after any
        # intermediate filtering steps.
        output_df = _filter_valid_recipes(output_df)
        output = output_df.to_dict("records")
        for recipe in output:
            recipe['RecipeIngredientParts'] = extract_quoted_strings(recipe['RecipeIngredientParts'])
            recipe['RecipeInstructions'] = extract_quoted_strings(recipe['RecipeInstructions'])
    else:
        output = None
    return output


class Generator:
    def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params
        self.dataset = load_dataset()

    def set_request(self, nutrition_input: list, ingredients: list, params: dict):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def generate(self):
        # Use local model instead of API call
        recommended = recommend(
            self.dataset,
            self.nutrition_input,
            self.ingredients,
            self.params
        )
        output = output_recommended_recipes(recommended)
        
        # Return in same format as API response
        class Response:
            def __init__(self):
                self.status_code = 200
                
            def json(self):
                return {'output': output}
        
        return Response()
