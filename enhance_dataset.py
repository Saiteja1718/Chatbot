import pandas as pd
import re

print("Loading dataset...")
df = pd.read_csv('Data/dataset.csv', compression='gzip')

print(f"Original dataset shape: {df.shape}")

# Define cuisine detection patterns
cuisine_patterns = {
    'Indian': [
        'curry', 'masala', 'tikka', 'tandoori', 'biryani', 'dal', 'paneer', 
        'naan', 'samosa', 'chutney', 'raita', 'korma', 'vindaloo', 'garam',
        'cardamom', 'turmeric', 'indian'
    ],
    'Japanese': [
        'sushi', 'sashimi', 'teriyaki', 'miso', 'wasabi', 'ramen', 'udon', 
        'tempura', 'katsu', 'edamame', 'dashi', 'japanese', 'sake'
    ],
    'Italian': [
        'pasta', 'spaghetti', 'linguine', 'penne', 'fettuccine', 'lasagna',
        'pizza', 'risotto', 'pesto', 'marinara', 'parmesan', 'mozzarella',
        'italian', 'ravioli', 'gnocchi', 'carbonara', 'alfredo'
    ],
    'Mexican': [
        'taco', 'burrito', 'enchilada', 'quesadilla', 'fajita', 'salsa',
        'guacamole', 'tortilla', 'mexican', 'nacho', 'tamale', 'chipotle',
        'jalapeño', 'poblano', 'cilantro'
    ],
    'Chinese': [
        'chow mein', 'lo mein', 'fried rice', 'spring roll', 'wonton',
        'szechuan', 'hunan', 'chinese', 'stir fry', 'hoisin', 'oyster sauce'
    ],
    'Thai': [
        'thai', 'pad thai', 'tom yum', 'green curry', 'red curry',
        'lemongrass', 'galangal', 'kaffir lime', 'basil thai'
    ],
    'Mediterranean': [
        'hummus', 'falafel', 'tahini', 'greek', 'mediterranean', 'tzatziki',
        'kebab', 'gyro', 'couscous', 'tabbouleh', 'pita', 'olive'
    ],
    'French': [
        'french', 'béarnaise', 'hollandaise', 'roux', 'quiche', 'crêpe',
        'croissant', 'brie', 'camembert', 'provence'
    ],
    'American': [
        'burger', 'bbq', 'barbecue', 'fried chicken', 'mac and cheese',
        'american', 'southern', 'cajun', 'buffalo'
    ]
}

print("\nDetecting cuisines...")

def detect_cuisine(row):
    """Detect cuisine type based on name and ingredients"""
    text = f"{row['Name']} {row['RecipeIngredientParts']}".lower()
    
    cuisine_scores = {}
    for cuisine, keywords in cuisine_patterns.items():
        score = sum(1 for keyword in keywords if keyword in text)
        if score > 0:
            cuisine_scores[cuisine] = score
    
    if cuisine_scores:
        # Return cuisine with highest score
        best_cuisine = max(cuisine_scores, key=cuisine_scores.get)
        # Only return if score is at least 2 for authenticity
        if cuisine_scores[best_cuisine] >= 2:
            return best_cuisine
        # Or if it's 1 but cuisine name is in the recipe name
        elif cuisine_scores[best_cuisine] >= 1 and best_cuisine.lower() in row['Name'].lower():
            return best_cuisine
    
    return 'Other'

# Apply cuisine detection
print("Processing recipes (this may take a few minutes)...")
df['Cuisine'] = df.apply(detect_cuisine, axis=1)

# Show statistics
print("\n" + "="*80)
print("CUISINE DISTRIBUTION:")
print("="*80)
cuisine_counts = df['Cuisine'].value_counts()
print(cuisine_counts)

# Show examples for each cuisine
print("\n" + "="*80)
print("SAMPLE RECIPES BY CUISINE:")
print("="*80)
for cuisine in ['Indian', 'Japanese', 'Italian', 'Mexican', 'Chinese', 'Thai', 'Mediterranean', 'French', 'American']:
    cuisine_recipes = df[df['Cuisine'] == cuisine]
    if len(cuisine_recipes) > 0:
        print(f"\n{cuisine} ({len(cuisine_recipes)} recipes):")
        for name in cuisine_recipes['Name'].head(5):
            print(f"  - {name}")

# Save enhanced dataset
print("\n" + "="*80)
print("SAVING ENHANCED DATASET...")
print("="*80)
output_file = 'Data/dataset_enhanced.csv'
df.to_csv(output_file, index=False, compression='gzip')
print(f"Saved to {output_file}")
print(f"Dataset now has {len(df.columns)} columns: {df.columns.tolist()}")
print(f"Total recipes: {len(df)}")
print("\nDone! Now update the code to use this enhanced dataset.")
