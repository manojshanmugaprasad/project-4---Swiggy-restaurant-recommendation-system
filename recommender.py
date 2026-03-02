import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load data once
cleaned_df = pd.read_csv("cleaned_data.csv")
encoded_df = pd.read_csv("encoded_data.csv")

with open("D:/swiggy recommendation system final/venv/Scripts/mlb.pkl", "rb") as f:
    mlb = pickle.load(f)

with open("D:/swiggy recommendation system final/venv/Scripts/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
    

def get_exact_matches(city, cuisines, rating, rating_count):
    mask = (
        (cleaned_df['city'] == city) &
        (cleaned_df['rating'] >= rating) &
        (cleaned_df['rating_count'] >= rating_count)
    )

    city_filtered = cleaned_df[mask]

    for cuisine in cuisines:
        city_filtered = city_filtered[
            city_filtered['cuisine'].str.contains(cuisine, case=False)
        ]

    return city_filtered


def get_suggestions(city, cuisines, rating, rating_count, top_n=5):

    city_mask = cleaned_df['city'] == city
    city_cleaned = cleaned_df[city_mask]
    city_encoded = encoded_df[city_mask]

    if city_encoded.empty:
        return pd.DataFrame()

    cuisine_vector = mlb.transform([cuisines])
    numeric_vector = scaler.transform([[rating, rating_count, 300]])

    input_vector = np.hstack([numeric_vector, cuisine_vector])

    similarity = cosine_similarity(input_vector, city_encoded)

    top_indices = similarity[0].argsort()[-top_n:][::-1]

    return city_cleaned.iloc[top_indices]