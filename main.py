import streamlit as st
import datetime

st.set_page_config(page_title="상세 사주 풀이", page_icon="🧧")
st.title("🧧 나의 상세 사주 풀이")

birth_date = st.date_input("🎂 생년월일을 입력하세요", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
gender = st.radio("👤 성별을 선택하세요", ["남성", "여성"])

# 사주 관련 기본 정보
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

# 간지 구하기
def get_ganji(year):
    gan = ten_gan[(year - 4) % 10]
    ji = twelve_ji[(year - 4) % 12]
    return gan + ji, gan, ji

def get_day_ganji(date):
    base = datetime.date(1900, 1, 1)
    days = (date - base).days
    gan = ten_gan[(days + 10) % 10]
    ji = twelve_ji[(days + 12) % 12]
    return gan + ji, gan, ji

def count_elements(*gans):
    result = {"목": 0, "화": 0, "토": 0, "금": 0, "수": 0}
    for g in gans:
        e = five_elements.get(g, "")
        if e:
            result[e] += 1
    return result

def count_yinyang(*gans):
    yin = sum(1 for g in gans if yin_yang.get(g) == "음")
    yang = sum(1 for g in gans if yin_yang.get(g) == "양")
    return {"음": yin, "양": yang}

if st.button("🔍 사주 분석 시작"):
    year, month, day = birth_date.year, birth_date.month, birth_date.day
    zodiac = zodiac_animals[(year - 4) % 12]

    # 연간지
    y_ganji, y_gan, y_ji = get_ganji(year)

    # 일간지
    d_ganji, d_gan, d_ji = get_day_ganji(birth_date)

    # 오행/음양 분석
    elements = count_elements(y_gan, d_gan)
    yin_yang_count = count_yinyang(y_gan, d_gan)

    st.header("🔢 기본 정보")
    st.markdown(f"""
    - 생년월일: **{year}년 {month}월 {day}일**
    - 띠(12지): **{zodiac}띠**
    - 성별: **{gender}**
    """)

    st.header("📜 사주 구성")
    st.markdown(f"""
    - 연간지: **{y_ganji}년생**
    - 일간지: **{d_ganji}**
    """)

    st.header("🌱 오행 분포 분석")
    for elem, cnt in elements.items():
        st.write(f"- {elem}의 기운: {cnt}개")
    strong = max(elements, key=elements.get)
    weak = min(elements, key=elements.get)
    st.markdown(f"👉 **가장 강한 오행:** {strong}, **가장 약한 오행:** {weak}")

    st.header("☯️ 음양 분석")
    st.markdown(f"""
    - 양 기운: {yin_yang_count['양']}개
    - 음 기운: {yin_yang_count['음']}개
    """)
    if abs(yin_yang_count['양'] - yin_yang_count['음']) >= 2:
        st.warning("⚠️ 음양의 균형이 다소 깨져 있습니다.")

    st.header("🧠 성격 및 기질 해석")
    if d_gan in five_elements:
        base_elem = five_elements[d_gan]
        explanation = {
            "목": "🌳 의지가 강하고 성장과 배움을 중시합니다. 인내와 융화력을 지닙니다.",
            "화": "🔥 열정과 추진력이 뛰어나며, 창의력과 개성이 돋보입니다.",
            "토": "⛰️ 안정감과 책임감이 강하며 중심을 잡는 역할을 잘 합니다.",
            "금": "⚔️ 논리적이고 냉철한 사고방식을 갖고 있으며, 정의로운 성격입니다.",
            "수": "💧 감수성이 풍부하고, 지혜롭고 유연한 사고를 갖습니다."
        }
        st.info(explanation[base_elem])

    st.header("🧾 종합 분석")
    st.markdown(f"""
    - 당신은 **{zodiac}띠**로, {y_gan}의 기운(오행: {five_elements.get(y_gan)})과 {d_gan}일주(오행: {five_elements.get(d_gan)})를 갖고 있습니다.
    - 오행의 분포상 **'{strong}'** 기운이 강하게 작용하며, **'{weak}'** 기운은 보완이 필요합니다.
    - 음양의 균형은 {'다소 불균형합니다.' if abs(yin_yang_count['양'] - yin_yang_count['음']) >= 2 else '적절하게 유지되고 있습니다.'}
    """)

    st.caption("📌 본 내용은 재미와 자기이해를 위한 참고용입니다.")
