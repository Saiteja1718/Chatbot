import numpy as np
import re


UNWANTED_NAME_KEYWORDS = [
    "clean out",
    "cleanout",
    "clean-out",
    "hot sauce",
]


def _filter_valid_recipes(df):
    if "Name" not in df.columns:
        return df

    mask = np.ones(len(df), dtype=bool)
    name_series = df["Name"].astype(str)
    for kw in UNWANTED_NAME_KEYWORDS:
        mask &= ~name_series.str.contains(kw, case=False, na=False).to_numpy()
    return df[mask]


def extract_data(dataframe,ingredients):
    extracted_data=dataframe.copy()
    extracted_data=_filter_valid_recipes(extracted_data)
    extracted_data=extract_ingredient_filtered_data(extracted_data,ingredients)
    return extracted_data
    
def extract_ingredient_filtered_data(dataframe,ingredients):
    extracted_data=dataframe.copy()
    regex_string=''.join(map(lambda x:f'(?=.*{x})',ingredients))
    extracted_data=extracted_data[extracted_data['RecipeIngredientParts'].str.contains(regex_string,regex=True,flags=re.IGNORECASE)]
    return extracted_data

def recommend(dataframe,_input,ingredients=[],params={'n_neighbors':5,'return_distance':False}):
        """
        Pure NumPy implementation equivalent to the original scikit-learn
        NearestNeighbors pipeline used by the FastAPI backend.
        """
        extracted_data = extract_data(dataframe, ingredients)
        k = params.get('n_neighbors', 5)

        if extracted_data.shape[0] < k:
            return None

        # Nutrition feature columns (consistent with frontend)
        features = extracted_data.iloc[:, 6:15].to_numpy(dtype=float)

        # Standardize features
        mean = features.mean(axis=0)
        std = features.std(axis=0)
        std[std == 0] = 1.0
        features_std = (features - mean) / std

        # Standardize input vector
        x = np.array(_input, dtype=float).reshape(1, -1)
        x_std = (x - mean) / std

        # Cosine similarity
        x_norm = np.linalg.norm(x_std, axis=1, keepdims=True)
        X_norm = np.linalg.norm(features_std, axis=1, keepdims=True)
        sim = (features_std @ x_std.T) / (X_norm * x_norm + 1e-12)

        top_k_idx = np.argsort(-sim[:, 0])[:k]
        return extracted_data.iloc[top_k_idx]

def extract_quoted_strings(s):
    # Find all the strings inside double quotes
    strings = re.findall(r'"([^"]*)"', s)
    # Join the strings with 'and'
    return strings

def output_recommended_recipes(dataframe):
    if dataframe is not None:
        output_df = dataframe.copy()
        output_df = _filter_valid_recipes(output_df)
        output=output_df.to_dict("records")
        for recipe in output:
            recipe['RecipeIngredientParts']=extract_quoted_strings(recipe['RecipeIngredientParts'])
            recipe['RecipeInstructions']=extract_quoted_strings(recipe['RecipeInstructions'])
    else:
        output=None
    return output

