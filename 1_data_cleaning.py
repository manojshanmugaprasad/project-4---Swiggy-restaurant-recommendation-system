import pandas as pd

df = pd.read_csv("D:/swiggy recommendation system/venv/Scripts/swiggy.csv")

print("Original shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()


# CLEAN RATING COLUMN


df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df = df[df['rating'].notna()]


# CLEAN COST COLUMN


df['cost'] = df['cost'].replace('[^0-9]', '', regex=True)
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
df = df[df['cost'].notna()]


# CLEAN RATING_COUNT COLUMN


df['rating_count'] = df['rating_count'].astype(str)
df['rating_count'] = df['rating_count'].replace('[^0-9]', '', regex=True)
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')
df['rating_count'] = df['rating_count'].fillna(0)


# HANDLE CATEGORICAL


df['city'] = df['city'].fillna("Unknown")
df['cuisine'] = df['cuisine'].fillna("Unknown")

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning completed successfully!")
print("New shape:", df.shape)
