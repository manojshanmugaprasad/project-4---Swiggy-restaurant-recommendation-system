import streamlit as st
import pandas as pd
import time
from Scripts.recommender import get_exact_matches, get_suggestions

st.set_page_config(
    page_title="Swiggy Recommender",
    page_icon="🍽",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.card {
    padding: 15px;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}
.card h4 {
    color: #FC8019;
}
.money-slider label {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load Data ----------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_data.csv")

df = load_data()

# ---------- Header Banner ----------
st.image("D:/swiggy recommendation system final/venv/Scripts/Food-02-1.png", use_container_width=True)

col1, col2 = st.columns([1, 6])

with col1:
    st.image("D:/swiggy recommendation system final/venv/Scripts/Swiggy-logo.jpg", width=200)

with col2:
    st.markdown(
        "<h1 style='color:#FC8019;'>Welcome to Swiggy Food Zone</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='color:gray;'>Discover restaurants that match your taste & budget</h4>",
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------- Filters ----------
st.subheader("🔎 Choose Your Preferences")

col1, col2, col3 = st.columns(3)

with col1:
    city = st.selectbox("🏙 Select City", sorted(df['city'].unique()))

city_df = df[df['city'] == city]

# Extract cuisines dynamically
cuisine_list = []
for item in city_df['cuisine']:
    for c in item.split(','):
        cuisine_list.append(c.strip())

unique_cuisines = sorted(set(cuisine_list))

with col2:
    selected_cuisines = st.multiselect(
        "🍜 Select Cuisine",
        unique_cuisines
    )

with col3:
    rating = st.slider("⭐ Minimum Rating", 1.0, 5.0, 4.0)

rating_count = st.number_input("👥 Minimum Rating Count", value=100)

# 💰 Cost Slider with currency formatting
cost = st.slider(
    "💰 Maximum Budget (₹ Cost for Two)",
    min_value=int(df['cost'].min()),
    max_value=int(df['cost'].max()),
    value=500,
    step=100
)

st.markdown("---")

# ---------- Recommendation ----------
if st.button("🚀 Find Restaurants"):

    if not selected_cuisines:
        st.warning("Please select at least one cuisine.")
    else:

        with st.spinner("🔍 Finding the best restaurants for you..."):
            time.sleep(1.5)  # Smooth animation feel

            exact_results = get_exact_matches(
                city,
                selected_cuisines,
                rating,
                rating_count
            )

            exact_results = exact_results[
                exact_results['cost'] <= cost
            ]

            suggestions = get_suggestions(
                city,
                selected_cuisines,
                rating,
                rating_count
            )

            suggestions = suggestions[
                suggestions['cost'] <= cost
            ]

        # ---------- Exact Matches ----------
        st.subheader("🎯 Exact Matches")

        if exact_results.empty:
            st.info("No exact matches found.")
        else:
            for _, row in exact_results.iterrows():
                st.markdown(f"""
                <div class="card">
                    <h4>{row['name']}</h4>
                    <p><b>City:</b> {row['city']}</p>
                    <p><b>Cuisine:</b> {row['cuisine']}</p>
                    <p>⭐ {row['rating']} | 👥 {row['rating_count']} ratings</p>
                    <p>💰 ₹{row['cost']} for two</p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")

        # ---------- Suggestions ----------
        st.subheader("⭐ Suggested Restaurants To Try")

        if suggestions.empty:
            st.info("No suggestions available.")
        else:
            for _, row in suggestions.iterrows():
                st.markdown(f"""
                <div class="card">
                    <h4>{row['name']}</h4>
                    <p><b>City:</b> {row['city']}</p>
                    <p><b>Cuisine:</b> {row['cuisine']}</p>
                    <p>⭐ {row['rating']} | 👥 {row['rating_count']} ratings</p>
                    <p>💰 ₹{row['cost']} for two</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
