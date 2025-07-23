import streamlit as st
import openai

st.set_page_config(page_title="심리 상담 도우미", page_icon="🧠")
st.title("🧠 마음 정리 챗봇")

st.write("당신의 마음을 글로 표현해 보세요. 제가 잘 정리해 드릴게요.")

# 감정 선택
emotion = st.selectbox("오늘의 감정에 가장 가까운 것을 골라주세요:", 
    ["불안", "슬픔", "분노", "외로움", "기쁨", "혼란", "무기력", "공허함", "설명하기 어려움"]
)

# 감정 서술
user_input = st.text_area("지금 어떤 생각이 드시나요? 자유롭게 적어보세요.", height=200)

# GPT 요약 및 위로 메시지 생성
if st.button("🧾 감정 정리 요청하기"):
    if user_input.strip() == "":
        st.warning("내용을 입력해주세요.")
    else:
        with st.spinner("감정을 정리하고 있습니다..."):
            # 여기서는 GPT-4 API를 사용하는 예시 (자신의 key 필요)
            openai.api_key = "YOUR_OPENAI_API_KEY"  # 안전하게 저장할 것
            prompt = f"""
당신은 따뜻하고 공감 어린 심리상담가입니다.
사용자가 자신의 감정을 아래와 같이 털어놓았습니다. 다음 형식으로 응답해주세요:

1. 감정 요약 (2~3줄)
2. 키워드 3~5개
3. 위로의 말 (짧고 문학적이거나 진심 어린 표현)

[사용자 입력]
"{user_input}"
"""
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8
            )
            result = response['choices'][0]['message']['content']
            st.markdown("### ✨ 분석 결과")
            st.markdown(result)

            st.info("💡 감정은 나를 해치기 위한 것이 아니라, 나를 알려주는 신호입니다.")
