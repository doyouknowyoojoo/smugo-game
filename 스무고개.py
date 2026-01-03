

# 20q_game.py

import streamlit as st



# --- 설정 ---

if "answer" not in st.session_state:

    st.session_state.answer = "삼겹살"  # 정답 설정

    st.session_state.hints = ["고기", "돼지고기", "구워 먹어요"]

    st.session_state.hint_count = 0

    st.session_state.history = []

    st.session_state.game_over = False



st.title("🧠 스무고개 AI 게임")

st.markdown("AI에게 질문을 하고 정답을 맞혀보세요! 질문은 20개까지 가능합니다.")



# --- 질문 입력 ---

with st.form("question_form"):

    user_question = st.text_input("질문을 입력하세요", "")

    submitted = st.form_submit_button("질문하기")



# --- 게임 로직 ---

def ai_answer(question):

    answer = st.session_state.answer

    st.session_state.history.append(("❓ " + question, ""))



    if question.strip() == "":

        return "질문을 입력해주세요."



    # 힌트 요청

    if "힌트" in question:

        if st.session_state.hint_count < 3:

            hint = st.session_state.hints[st.session_state.hint_count]

            st.session_state.hint_count += 1

            return f"💡 힌트 {st.session_state.hint_count}: {hint}"

        else:

            return "⚠️ 힌트는 최대 3개까지 제공됩니다."



    # 정답 맞히기

    if question.strip() == answer:

        st.session_state.game_over = True

        return "✅ 정답입니다."



    # 예/아니오/모호 판단 예시 로직 (간단한 키워드 기반)

    # 실제론 LLM 응답이 좋지만 여기선 고정 규칙

    keywords = {

        "고기": "네", "채소": "아니오", "음식": "네", "불": "네", "돼지": "네",

        "차가워": "아니오", "디저트": "아니오", "식물": "아니오", "국물": "아니오"

    }



    for word, reply in keywords.items():

        if word in question:

            return reply



    return "질문이 모호합니다."



# --- 질문 처리 ---

if submitted and not st.session_state.game_over:

    response = ai_answer(user_question)

    st.session_state.history[-1] = (st.session_state.history[-1][0], response)



# --- 기록 표시 ---

st.markdown("### 💬 질문 기록")

for q, a in st.session_state.history:

    st.write(f"{q}")

    if a:

        st.write(f"🧠 {a}")



# --- 게임 종료 시 메시지 ---

if st.session_state.game_over:

    st.success("🎉 축하합니다! 정답을 맞히셨습니다.")