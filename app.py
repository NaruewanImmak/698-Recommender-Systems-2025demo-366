import streamlit as st
import pickle
import os
import gdown
from myfunction_66130700366 import get_movie_recommendations

# ===== Config download file from Google Drive =====
FILE_ID = "1faPaNG7BVKKl0WdkXdsOhoBGwi_UB5HO"
FILE_URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
FILE_NAME = "recommendation_data.pkl"


@st.cache_resource
def load_data():
    # ถ้ายังไม่มีไฟล์ในโฟลเดอร์ ให้โหลดจาก Google Drive มาก่อน
    if not os.path.exists(FILE_NAME):
        gdown.download(FILE_URL, FILE_NAME, quiet=False)

    # โหลดข้อมูลจากไฟล์ .pkl
    with open(FILE_NAME, "rb") as file:
        user_similarity_df, user_movie_ratings = pickle.load(file)

    return user_similarity_df, user_movie_ratings


# โหลดข้อมูลครั้งเดียว
user_similarity_df, user_movie_ratings = load_data()

# ===== Streamlit UI =====
st.title("🎬 Movie Recommendation System")
st.write("ระบบแนะนำภาพยนตร์แบบ Collaborative Filtering")

# ให้ผู้ใช้กรอก User ID
user_id = st.number_input("กรอก User ID:", min_value=1, step=1)

if st.button("แนะนำหนังให้ฉันเลย!"):
    try:
        recommendations = get_movie_recommendations(
            user_id, user_similarity_df, user_movie_ratings, 10
        )

        st.subheader(f"📌 Top 10 Movie Recommendations for User {user_id}")
        for idx, movie_title in enumerate(recommendations, start=1):
            st.write(f"**{idx}.** {movie_title}")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
