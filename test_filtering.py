import pandas as pd
import re

# Load dataset
df = pd.read_csv('Data/dataset.csv', compression='gzip')

print("Testing cuisine filtering logic...\n")

# Test Indian cuisine filtering
indian_keywords = ['curry', 'garam', 'masala', 'cumin', 'turmeric', 'coriander', 
                  'cardamom', 'tandoori', 'tikka', 'biryani', 'paneer', 'naan',
                  'dal', 'samosa', 'chutney', 'raita', 'korma', 'vindaloo']

print("="*80)
print("TESTING INDIAN CUISINE FILTER")
print("="*80)

# Test strict filtering (2+ keywords)
test_recipes = df.head(1000)  # Test on first 1000 recipes
strict_matches = []

for idx, row in test_recipes.iterrows():
    recipe_name = row['Name'].lower()
    recipe_ingredients = str(row['RecipeIngredientParts']).lower()
    recipe_text = f"{recipe_name} {recipe_ingredients}"
    
    match_count = sum(1 for keyword in indian_keywords if keyword.lower() in recipe_text)
    
    if match_count >= 2:
        strict_matches.append((row['Name'], match_count))

print(f"\nFound {len(strict_matches)} recipes with 2+ Indian keywords")
print("\nTop 10 matches:")
for name, score in sorted(strict_matches, key=lambda x: x[1], reverse=True)[:10]:
    print(f"  Score {score}: {name}")

# Test lenient filtering (1+ keyword)
lenient_matches = []
for idx, row in test_recipes.iterrows():
    recipe_name = row['Name'].lower()
    recipe_ingredients = str(row['RecipeIngredientParts']).lower()
    recipe_text = f"{recipe_name} {recipe_ingredients}"
    
    match_count = sum(1 for keyword in indian_keywords if keyword.lower() in recipe_text)
    
    if match_count >= 1:
        lenient_matches.append((row['Name'], match_count))

print(f"\nFound {len(lenient_matches)} recipes with 1+ Indian keywords")

# Test on whole dataset for Indian
print("\n" + "="*80)
print("FULL DATASET INDIAN SEARCH")
print("="*80)
indian_in_dataset = []
for idx, row in df.iterrows():
    recipe_name = row['Name'].lower()
    recipe_ingredients = str(row['RecipeIngredientParts']).lower()
    recipe_text = f"{recipe_name} {recipe_ingredients}"
    
    match_count = sum(1 for keyword in indian_keywords if keyword.lower() in recipe_text)
    
    if match_count >= 2:
        indian_in_dataset.append((row['Name'], match_count))
    
    if len(indian_in_dataset) >= 50:  # Get first 50
        break

print(f"Found {len(indian_in_dataset)} Indian recipes (stopped at 50)")
print("\nSample Indian recipes found:")
for name, score in indian_in_dataset[:15]:
    print(f"  Score {score}: {name}")
