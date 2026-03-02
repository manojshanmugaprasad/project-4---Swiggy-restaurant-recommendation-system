import pandas as pd
import pickle
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler

# Load cleaned data
df = pd.read_csv("D:/swiggy recommendation system final/cleaned_data.csv")

# Split cuisines (assuming comma separated)
df['cuisine'] = df['cuisine'].apply(lambda x: x.split(','))

# MultiLabelBinarizer for cuisine
mlb = MultiLabelBinarizer()
cuisine_encoded = mlb.fit_transform(df['cuisine'])

cuisine_df = pd.DataFrame(cuisine_encoded, columns=mlb.classes_)

# Scale numerical features
scaler = StandardScaler()
numerical = scaler.fit_transform(df[['rating', 'rating_count', 'cost']])
numerical_df = pd.DataFrame(numerical, columns=['rating', 'rating_count', 'cost'])

# Combine features
encoded_df = pd.concat([numerical_df, cuisine_df], axis=1)

# Save encoded data
encoded_df.to_csv("encoded_data.csv", index=False)

# Save models
with open("D:/swiggy recommendation system final/venv/Scripts/mlb.pkl", "wb") as f:
    pickle.dump(mlb, f)

with open("D:/swiggy recommendation system final/venv/Scripts/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Preprocessing completed.")