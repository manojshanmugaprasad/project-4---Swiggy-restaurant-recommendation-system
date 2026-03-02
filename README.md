Swiggy Restaurant Recommendation System using Streamlit

This project develops a hybrid restaurant recommendation system using a real-world Swiggy dataset and deploys it through an interactive Streamlit web application. The system recommends restaurants based on user preferences such as city (mandatory), cuisine (multi-select), minimum rating, rating count, and budget.

The recommendation pipeline combines filter-based matching and cosine similarity-based suggestions. Exact matches are generated using strict filtering on user inputs, while additional suggestions are ranked using cosine similarity within the selected city to ensure locality-aware personalization.

Data preprocessing involved cleaning non-numeric values (₹, K, + symbols), handling missing data, and encoding multi-cuisine features using MultiLabelBinarizer. Numerical features were normalized using StandardScaler to improve similarity computation accuracy. Performance was optimized by computing similarity dynamically within city-level subsets and using Streamlit caching for smooth interaction.

The final dashboard features a Swiggy-themed UI with banner integration, animated loading spinner, budget slider, and restaurant cards for structured result display.

Technologies Used

Python • Pandas • NumPy • Scikit-Learn • Streamlit • Cosine Similarity • MultiLabelBinarizer • StandardScaler
