import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="심리 상담 도우미", page_icon="🧠")
st.title("🧠 마음 정리 챗봇")
st.write("당신의 마음을 자유롭게 표현해 보세요. 제가 잘 들어드릴게요.")

# 감정 선택
emotion = st.selectbox("오늘의 감정에 가장 가까운 것은?", 
    ["불안", "슬픔", "분노", "외로움", "기쁨", "혼란", "무기력", "공허함", "설명하기 어려움"]
)

# 고민 서술
user_input = st.text_area("지금 어떤 생각이 드시나요? 자유롭게 적어보세요.", height=200)

# 분석 실행
if st.button("🔍 감정 정리 요청하기"):
    if not user_input.strip():
        st.warning("내용을 입력해주세요.")
    else:
        # 키워드 추출 (가장 많이 나온 단어 3개)
        words = re.findall(r'\b[가-힣a-zA-Z]{2,}\b', user_input)
        top_keywords = [w for w, _ in Counter(words).most_common(3)]

        # 감정 유형별 위로 문장
        comfort_dict = {
            "불안": "지금 느끼는 불안은 당신의 마음이 조심스럽게 세상을 바라보는 방식일지도 몰라요.",
            "슬픔": "슬픔은 마음의 회복을 위한 시간일 수 있어요. 천천히 숨 쉬어요.",
            "분노": "화를 낸다는 건 당신의 경계가 침해되었다는 신호일지도 몰라요. 당신은 존중받아야 해요.",
            "외로움": "외로움은 연결을 원하는 자연스러운 감정이에요. 당신은 혼자가 아니에요.",
            "기쁨": "그 기쁨, 마음껏 누려도 돼요. 좋은 일은 당신에게도 어울려요.",
            "혼란": "지금 혼란스럽더라도 결국엔 방향을 찾게 될 거예요. 조급하지 않아도 괜찮아요.",
            "무기력": "아무것도 하기 싫은 날이 있어요. 그럴 땐 그냥 숨 쉬는 것도 충분해요.",
            "공허함": "공허함은 마음에 빈자리가 생긴 신호예요. 무언가 새로운 것이 들어올 준비를 하는 거예요.",
            "설명하기 어려움": "말로 표현하기 어려운 감정도, 충분히 유효하고 소중해요."
        }

        st.markdown("### 📝 감정 요약")
        st.write(f"- 선택한 감정: **{emotion}**")
        st.write(f"- 고민 키워드: {', '.join(top_keywords) if top_keywords else '명확한 키워드 없음'}")

        st.markdown("### 💬 위로의 말")
        st.info(comfort_dict.get(emotion, "마음을 잘 들었습니다. 스스로에게 너무 엄격하지 않아도 돼요."))

        st.caption("💡 감정을 말로 꺼내는 것만으로도 치유가 시작됩니다.")
