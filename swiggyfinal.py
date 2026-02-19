import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# PAGE CONFIG

st.set_page_config(
    page_title="Swiggy Recommendation System",
    layout="wide",
    page_icon="🍽️"
)


# LOAD DATA

cleaned_df = pd.read_csv("cleaned_data.csv")
encoded_df = pd.read_csv("encoded_data.csv")


# HEADER SECTION (LOGO + TITLE)

col1, col2 = st.columns([1, 5])

with col1:
    logo = Image.open("D:/swiggy recommendation system/venv/Scripts/images.png")
    st.image(logo, width=150)

with col2:
    st.title("Welcome to SWIGGY Food Zone and Popular Pick")
    st.markdown("Discover restaurants based on your preferences")

st.markdown("---")


# BANNER IMAGE

banner = Image.open("D:/swiggy recommendation system/venv/Scripts/delicious-indian-meal-with-biryani-rice-photo.jpeg")
st.image(banner, use_container_width=True)

st.markdown("---")


# SIDEBAR FILTERS

st.sidebar.header("Filter Preferences")

city = st.sidebar.selectbox(
    "Select City",
    sorted(cleaned_df['city'].unique())
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    sorted(cleaned_df['cuisine'].unique())
)

min_rating = st.sidebar.slider(
    "Minimum Rating",
    1.0, 5.0, 3.5
)

min_rating_count = st.sidebar.slider(
    "Minimum Rating Count",
    min_value=0,
    max_value=int(cleaned_df['rating_count'].max()),
    value=50
)


max_cost = st.sidebar.number_input(
    "Maximum Cost (₹)",
    min_value=0,
    value=500
)


# RECOMMENDATION BUTTON

if st.sidebar.button("🔎 Get Recommendations"):

    filtered = cleaned_df[
    (cleaned_df['city'] == city) &
    (cleaned_df['cuisine'] == cuisine) &
    (cleaned_df['rating'] >= min_rating) &
    (cleaned_df['cost'] <= max_cost) &
    (cleaned_df['rating_count'] >= min_rating_count)
]


    if filtered.empty:
        st.warning("No restaurants match your preferences. Try adjusting filters.")
    else:

        filtered_indices = filtered.index.tolist()
        encoded_filtered = encoded_df.loc[filtered_indices]

        selected_vector = encoded_filtered.iloc[0].values.reshape(1, -1)
        similarities = cosine_similarity(selected_vector, encoded_filtered)

        similarity_scores = list(enumerate(similarities[0]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        top_indices_local = [i[0] for i in similarity_scores[1:6]]
        top_indices_global = [filtered_indices[i] for i in top_indices_local]

        recommendations = cleaned_df.loc[top_indices_global]

        st.markdown("## 🍽️ Top Recommended Restaurants")

        for _, row in recommendations.iterrows():
            st.markdown(f"""
            <div style="
                padding:15px;
                border-radius:10px;
                border:1px solid #f0f0f0;
                margin-bottom:15px;
                background-color:#fafafa;
            ">
            <h4>{row['name']}</h4>
            <p>📍 <b>City:</b> {row['city']}</p>
            <p>🍴 <b>Cuisine:</b> {row['cuisine']}</p>
            <p>⭐ <b>Rating:</b> {row['rating']}</p>
            <p>💰 <b>Cost:</b> ₹{row['cost']}</p>
            </div>
            """, unsafe_allow_html=True)
