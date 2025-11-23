import streamlit as st
import pickle
import os
import gdown
from myfunction_66130700366 import get_movie_recommendations

# ===== Config download file from Google Drive =====
FILE_ID = "1faPaNG7BVKKl0WdkXdsOhoBGwi_UB5HO"
FILE_NAME = "recommendation_data.pkl"


@st.cache_resource
def load_data():
    # ถ้ายังไม่มีไฟล์ในโฟลเดอร์ ให้โหลดจาก Google Drive มาก่อน
    if not os.path.exists(FILE_NAME):
        # ใช้ id โดยตรง จะเสถียรกว่าใช้ URL ยาวๆ
        gdown.download(id=FILE_ID, output=FILE_NAME, quiet=False)

    # โหลดข้อมูลจากไฟล์ .pkl
    with open(FILE_NAME, "rb") as file:
        user_similarity_df, user_movie_ratings = pickle.load(file)

    return user_similarity_df, user_movie_ratings
