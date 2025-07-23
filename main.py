import streamlit as st
import random

st.set_page_config(page_title="오늘 점심 뭐 먹지?", page_icon="🍱")

st.title("🍽️ 오늘 점심 뭐 먹지?")
st.write("점심 메뉴 선택이 고민될 때, 한 번 눌러보세요!")

# 기본 메뉴
default_menus = {
    "한식": ["비빔밥", "김치찌개", "된장찌개", "불고기", "삼겹살", "순두부찌개", "국밥"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "볶음밥"],
    "일식": ["초밥", "라멘", "돈부리", "가츠동", "우동"],
    "양식": ["파스타", "피자", "햄버거", "스테이크", "샐러드"],
    "기타": ["분식", "도시락", "샌드위치", "컵밥", "편의점"]
}

# 세션 상태 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()

if "excluded" not in st.session_state:
    st.session_state.excluded = []

# 카테고리 선택
selected_categories = st.multiselect(
    "🍱 먹고 싶은 카테고리를 선택하세요", options=list(st.session_state.menus.keys()),
    default=list(st.session_state.menus.keys())
)

# 제외할 메뉴 선택
all_menus = [menu for cat in selected_categories for menu in st.session_state.menus[cat]]
excluded_menus = st.multiselect("❌ 제외할 메뉴가 있다면 선택하세요", options=all_menus)

# 메뉴 추천
if st.button("✅ 메뉴 추천받기"):
    candidate_menus = [menu for cat in selected_categories for menu in st.session_state.menus[cat]
                       if menu not in excluded_menus]
    if candidate_menus:
        choice = random.choice(candidate_menus)
        st.success(f"오늘의 추천 메뉴는... **{choice}** 입니다! 😋")
    else:
        st.warning("선택된 메뉴가 없어요. 카테고리나 제외 목록을 다시 확인해 주세요.")

# 메뉴 직접 추가
with st.expander("➕ 직접 메뉴 추가하기"):
    new_menu = st.text_input("추가할 메뉴 이름")
    new_category = st.selectbox("카테고리 선택", options=list(st.session_state.menus.keys()))
    if st.button("메뉴 추가"):
        if new_menu:
            st.session_state.menus[new_category].append(new_menu)
            st.success(f"{new_category}에 '{new_menu}' 메뉴를 추가했어요!")
        else:
            st.warning("메뉴 이름을 입력해 주세요.")

# 현재 메뉴 확인
with st.expander("📋 현재 등록된 메뉴 보기"):
    for cat, items in st.session_state.menus.items():
        st.markdown(f"**{cat}**: {', '.join(items)}")

# 공유용 텍스트 생성
if st.button("📋 결과 복사용 텍스트 생성"):
    if 'choice' in locals():
        st.code(f"오늘 점심은 {choice} 어때요?")
    else:
        st.info("먼저 메뉴 추천을 받아주세요.")

