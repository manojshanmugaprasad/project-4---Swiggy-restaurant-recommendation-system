Swiggy Restaurant Recommendation System using Streamlit

This project builds a Restaurant Recommendation System using a real-world Swiggy dataset and deploys it as an interactive Streamlit web application. The system recommends restaurants based on user preferences such as city, cuisine, minimum rating, maximum cost, and minimum rating count. The objective is to help users discover relevant restaurants in a structured and personalized manner while improving decision-making through filtered recommendations.

The workflow involved data cleaning, preprocessing, and feature engineering. Duplicate records were removed, non-numeric values in rating, cost, and rating_count columns were cleaned, and missing values were handled properly. Categorical features like city and cuisine were encoded using One-Hot Encoding, while numerical features were retained for similarity computation. Cosine Similarity was used as the core recommendation methodology. To ensure scalability and avoid memory issues, similarity was computed dynamically within filtered subsets rather than generating a full similarity matrix.

The Streamlit application provides a user-friendly interface where users can select their preferences through sidebar filters. Based on these inputs, the system filters relevant restaurants, computes similarity, and displays the top recommendations in a structured layout. The project demonstrates practical skills in data preprocessing, similarity-based recommendation systems, performance optimization, and interactive web app development, making it aligned with real-world recommendation system applications.

Technologies Used
Python
Pandas
NumPy
Scikit-Learn
Streamlit
Cosine Similarity
One-Hot Encoding
