import streamlit as st
import pickle
import gdown
import os

# Google Drive File Info
FILE_ID = "1faPaNG7BVKKl0WdkXdsOhoBGwi_UB5HO"
FILE_NAME = "recommendation_data.pkl"

# Download from Google Drive if not exists
def load_data():
    if not os.path.exists(FILE_NAME):
        st.write("📥 Downloading data from Google Drive...")
        gdown.download(id=FILE_ID, output=FILE_NAME, quiet=False)

    with open(FILE_NAME, "rb") as file:
        return pickle.load(file)

# Load Data
user_similarity_df, user_movie_ratings = load_data()

# Streamlit UI
st.title("🎬 Movie Recommendation System")

# User selection
user_ids = user_movie_ratings.index.tolist()
user_id = st.selectbox("Select a User ID:", user_ids)

# Number of recommendations
num_recommendations = st.slider("Number of Recommendations", 1, 20, 10)

# Button to get recommendations
if st.button("Get Recommendations"):
    from myfunction_66130700366 import get_movie_recommendations

    recommendations = get_movie_recommendations(
        user_id,
        user_similarity_df,
        user_movie_ratings,
        num_recommendations
    )

    st.subheader(f"Top {num_recommendations} Movie Recommendations for User {user_id}:")
    for i, title in enumerate(recommendations, start=1):
        st.write(f"{i}. {title}")
