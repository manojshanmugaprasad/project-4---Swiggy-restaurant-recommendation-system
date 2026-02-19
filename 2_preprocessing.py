import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle

# Load cleaned data
df = pd.read_csv("D:/swiggy recommendation system/cleaned_data.csv")

# Columns to encode
categorical_cols = ['city', 'cuisine']

# Create encoder
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

encoded_features = encoder.fit_transform(df[categorical_cols])

encoded_df = pd.DataFrame(
    encoded_features,
    columns=encoder.get_feature_names_out(categorical_cols)
)

# Add numerical columns
numerical_df = df[['rating', 'rating_count', 'cost']].reset_index(drop=True)

final_df = pd.concat([numerical_df, encoded_df], axis=1)

# Save encoded dataset
final_df.to_csv("encoded_data.csv", index=False)

# Save encoder
with open("encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("Preprocessing completed successfully!")
