import pandas as pd

# Load dataset
df = pd.read_csv('Data/dataset.csv', compression='gzip')

print("="*80)
print("DATASET ANALYSIS")
print("="*80)
print(f"\nDataset shape: {df.shape}")
print(f"\nColumn names:\n{df.columns.tolist()}")

print("\n" + "="*80)
print("SAMPLE RECIPE NAMES (First 50):")
print("="*80)
for i, name in enumerate(df['Name'].head(50), 1):
    print(f"{i:2d}. {name}")

print("\n" + "="*80)
print("CHECKING FOR CUISINE INDICATORS:")
print("="*80)

# Check for Indian recipes
indian_keywords = ['curry', 'masala', 'tikka', 'tandoori', 'biryani', 'dal', 'indian']
indian_recipes = df[df['Name'].str.contains('|'.join(indian_keywords), case=False, regex=True)]
print(f"\nRecipes with Indian keywords: {len(indian_recipes)}")
print("Sample Indian recipes:")
for name in indian_recipes['Name'].head(10):
    print(f"  - {name}")

# Check for Japanese recipes  
japanese_keywords = ['sushi', 'teriyaki', 'miso', 'japanese', 'ramen', 'udon']
japanese_recipes = df[df['Name'].str.contains('|'.join(japanese_keywords), case=False, regex=True)]
print(f"\nRecipes with Japanese keywords: {len(japanese_recipes)}")
print("Sample Japanese recipes:")
for name in japanese_recipes['Name'].head(10):
    print(f"  - {name}")

# Check for Italian recipes
italian_keywords = ['pasta', 'italian', 'parmesan', 'marinara', 'pesto', 'pizza', 'lasagna']
italian_recipes = df[df['Name'].str.contains('|'.join(italian_keywords), case=False, regex=True)]
print(f"\nRecipes with Italian keywords: {len(italian_recipes)}")
print("Sample Italian recipes:")
for name in italian_recipes['Name'].head(10):
    print(f"  - {name}")

# Check for Mexican recipes
mexican_keywords = ['taco', 'burrito', 'mexican', 'enchilada', 'quesadilla', 'salsa']
mexican_recipes = df[df['Name'].str.contains('|'.join(mexican_keywords), case=False, regex=True)]
print(f"\nRecipes with Mexican keywords: {len(mexican_recipes)}")
print("Sample Mexican recipes:")
for name in mexican_recipes['Name'].head(10):
    print(f"  - {name}")

print("\n" + "="*80)
print("SAMPLE INGREDIENTS (from first recipe):")
print("="*80)
if 'RecipeIngredientParts' in df.columns:
    print(df['RecipeIngredientParts'].iloc[0])
