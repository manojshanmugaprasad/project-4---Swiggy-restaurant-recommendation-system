import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
cleaned_df = pd.read_csv("D:/swiggy recommendation system/cleaned_data.csv")
encoded_df = pd.read_csv("D:/swiggy recommendation system/encoded_data.csv")

# Compute similarity

def recommend(index, top_n=5):
    selected_vector = encoded_df.iloc[index].values.reshape(1, -1)

    similarities = cosine_similarity(selected_vector, encoded_df)

    similarity_scores = list(enumerate(similarities[0]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similarity_scores = similarity_scores[1:top_n+1]
    indices = [i[0] for i in similarity_scores]

    return cleaned_df.iloc[indices]


# Test
print(recommend(0))
