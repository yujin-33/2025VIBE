import streamlit as st
import datetime

st.set_page_config(page_title="사주 봐주는 앱", page_icon="🔮")
st.title("🔮 나의 사주 카드")

birth_date = st.date_input("생년월일을 선택하세요", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
gender = st.radio("성별", ["남성", "여성"])

# 간지 및 오행/음양 정보
ten_gan = ["갑", "을", "병", "정", "무", "기", "경", "신", "임", "계"]
twelve_ji = ["자", "축", "인", "묘", "진", "사", "오", "미", "신", "유", "술", "해"]
zodiac_animals = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]
five_elements = {
    "갑": "목", "을": "목", "병": "화", "정": "화",
    "무": "토", "기": "토", "경": "금", "신": "금",
    "임": "수", "계": "수"
}
yin_yang = {
    "갑": "양", "을": "음", "병": "양", "정": "음",
    "무": "양", "기": "음", "경": "양", "신": "음",
    "임": "양", "계": "음"
}

def get_ganji(year):
    gan = ten_gan[(year - 4) % 10]
    ji = twelve_ji[(year - 4) % 12]
    return gan + ji, gan, ji

def get_zodiac(year):
    return zodiac_animals[(year - 4) % 12]

def get_day_ganji(date):
    days_since_base = (date - datetime.date(1900, 1, 1)).days
    gan = ten_gan[(days_since_base + 10) % 10]
    ji = twelve_ji[(days_since_base + 12) % 12]
    return gan + ji, gan, ji

# 결과 출력
if st.button("🔍 나의 사주카드 보기"):
    year = birth_date.year
    month = birth_date.month
    day = birth_date.day

    year_ganji, y_gan, y_ji = get_ganji(year)
    zodiac = get_zodiac(year)
    day_ganji, d_gan, d_ji = get_day_ganji(birth_date)
    element = five_elements.get(d_gan, "알 수 없음")
    yin_or_yang = yin_yang.get(d_gan, "알 수 없음")

    # 카드 스타일 HTML로 예쁘게 표현
    card_html = f"""
    <div style='
        background: linear-gradient(to right, #fdfbfb, #ebedee);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        max-width: 500px;
        margin: 0 auto;
        font-family: "Nanum Gothic", sans-serif;
        text-align: center;
        line-height: 1.6;
    '>
        <h2 style='margin-bottom: 0.3em;'>🔮 나의 사주 카드 🔮</h2>
        <hr style='margin-bottom: 1em;' />
        <h3>🧑 성별: {gender}</h3>
        <h3>📅 생년월일: {year}년 {month}월 {day}일</h3>
        <h3>🐾 띠: {zodiac}띠 ({y_ji})</h3>
        <h3>📜 연간지: {year_ganji}</h3>
        <h3>🗓️ 일간지: {day_ganji}</h3>
        <h3>☯️ 음양: {yin_or_yang}</h3>
        <h3>🌟 오행 기운: {element}</h3>
        <hr />
        <p style='font-size: 0.95rem; color: #444;'>⚠️ 이 결과는 참고용입니다. 정확한 해석은 전문가에게 문의하세요.</p>
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)



