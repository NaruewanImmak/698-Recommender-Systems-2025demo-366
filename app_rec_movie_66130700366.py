
import streamlit as st
import pickle
from myfunction_66130700366 import get_movie_recommendations

# โหลดข้อมูล recommendation_data.pkl
with open('recommendation_data.pkl', 'rb') as file:
    user_similarity_df, user_movie_ratings = pickle.load(file)

# ส่วนหัวของเว็บ
st.title("🎬 Movie Recommendation System")
st.write("ระบบแนะนำภาพยนตร์ด้วย Collaborative Filtering (User-based)")

# ช่องให้กรอก user_id
user_id = st.number_input("กรอก User ID", min_value=1, step=1)

# ปุ่มกดเพื่อแสดงผลลัพธ์
if st.button("แนะนำภาพยนตร์"):
    recommendations = get_movie_recommendations(user_id, user_similarity_df, user_movie_ratings, 10)
    if len(recommendations) > 0:
        st.subheader(f"Top 10 ภาพยนตร์แนะนำสำหรับ User {user_id}")
        for idx, movie_title in enumerate(recommendations, 1):
            st.write(f"{idx}. {movie_title}")
    else:
        st.warning("ไม่พบข้อมูลการแนะนำสำหรับผู้ใช้นี้ค่ะ")

# เพิ่มเครดิตท้ายหน้า
st.markdown("---")
st.caption("สร้างโดย 66130700366 | Workshop Recommendation System")

