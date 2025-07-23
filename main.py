import streamlit as st

st.title("🎽 상황별 옷 코디 추천기")

# 사용자 입력
situation = st.text_input("상황을 입력하세요", placeholder="예: 소개팅, 친구 만남, 회사 면접 등")
gender = st.radio("성별을 선택하세요", ["남성", "여성"])
season = st.selectbox("계절을 선택하세요", ["봄", "여름", "가을", "겨울"])
tone = st.selectbox("원하는 색상 톤을 선택하세요", ["톤온톤", "무채색", "파스텔", "원색"])

if st.button("코디 추천받기"):
    top, bottom = recommend_outfit(situation, gender, season, tone)
    st.subheader("✨ 추천 코디")
    st.write(f"**상의:** {top}")
    st.write(f"**하의:** {bottom}")
