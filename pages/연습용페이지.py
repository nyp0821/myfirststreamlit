# import streamlit as st

# st.title("형성평가")

# option = st.radio("정답은 무엇일까요?", ["강남역", "교대역", "서초역", "선릉역", "5"])
# if option=="강남역":
#     st.success("정답입니다")

# option1 = st.multiselect("연수장소는 어디일까요?", ["강남역", "교대역", "서초역", "선릉역", "5"])

# agree = st.checkbox("동의하시나요?")

# if agree:
#     st.write("동의하셨군요")
# else:
#     st.write("동의해주세요")

# import streamlit as st

# # 페이지 제목 및 설명
# st.title("형성평가")
# st.subheader("퀴즈에 도전하고 결과를 확인해보세요!")

# # 첫 번째 질문 (정답을 선택하는 라디오 버튼)
# st.write("### 1. 정답은 무엇일까요?")
# option = st.radio("정답을 선택하세요:", ["강남역", "교대역", "서초역", "선릉역", "5"])
# if option == "강남역":
#     st.success("정답입니다! 강남역은 대한민국의 대표적인 지하철역 중 하나입니다.")
# else:
#     st.error("틀렸습니다! 다시 시도해보세요.")

# # 두 번째 질문 (연수 장소 선택)
# st.write("### 2. 연수장소는 어디일까요?")
# option1 = st.multiselect("여러 장소를 선택할 수 있습니다.", ["강남역", "교대역", "서초역", "선릉역", "5"])
# if option1:
#     st.info(f"선택하신 장소: {', '.join(option1)}")
# else:
#     st.warning("장소를 하나 이상 선택해주세요.")

# # 동의 여부 체크박스
# st.write("### 3. 약관에 동의하시나요?")
# agree = st.checkbox("동의하기")
# if agree:
#     st.write("동의해주셔서 감사합니다!")
# else:
#     st.warning("동의해주세요.")

# # 사용자 입력 요약
# st.write("### 입력 내용 확인")
# st.write(f"- 선택한 정답: {option}")
# st.write(f"- 선택한 연수 장소: {', '.join(option1) if option1 else '선택 안 함'}")
# st.write(f"- 동의 여부: {'동의함' if agree else '동의하지 않음'}")

# # 최종 메시지
# st.write("형성평가에 참여해주셔서 감사합니다!")


import streamlit as st
import random

# 페이지 제목
st.title("숫자 맞추기 게임 🎯")

# 설명 텍스트
st.write("컴퓨터가 1부터 100 사이에서 무작위로 숫자를 선택합니다. 그 숫자를 맞춰보세요!")

# 컴퓨터가 고른 숫자 저장 (세션 상태 사용)
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)

# 사용자 입력 (숫자)
user_guess = st.number_input("숫자를 입력하세요 (1~100):", min_value=1, max_value=100, step=1)

# 시도 횟수 세기 (세션 상태 사용)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# 버튼을 클릭하면 시도 횟수를 증가시키고 결과를 확인
if st.button("확인"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.random_number:
        st.warning(f"너무 낮습니다! 시도 횟수: {st.session_state.attempts}")
    elif user_guess > st.session_state.random_number:
        st.warning(f"너무 높습니다! 시도 횟수: {st.session_state.attempts}")
    else:
        st.success(f"정답입니다! {st.session_state.attempts}번 만에 맞췄어요!")
        st.balloons()  # 정답 맞추면 축하 애니메이션
        # 게임이 끝나면 새로운 숫자 생성
        if st.button("다시 시작하기"):
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0

# 개발자 팁
st.sidebar.title("게임 팁 💡")
st.sidebar.write("""
1. 숫자를 최대한 좁혀보세요!
2. 너무 높은 숫자를 입력하면 낮은 쪽을 시도해 보세요.
3. 숫자 범위를 줄이면서 추측을 진행해 보세요.
""")



