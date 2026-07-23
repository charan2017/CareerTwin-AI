import random
import streamlit as st

from utils.interview_questions import QUESTIONS
from utils.interview_score import evaluate_answer


def show_interview():

    st.divider()
    st.header("🎤 AI Interview Simulator")

    role = st.selectbox(
        "Choose Interview Role",
        list(QUESTIONS.keys()),
        key="interview_role"
    )

    if st.button(
        "🎲 Generate Interview Question",
        key="generate_question"
    ):

        question = random.choice(QUESTIONS[role])
        st.session_state["question"] = question

    if "question" in st.session_state:

        question = st.session_state["question"]

        st.subheader("Interview Question")
        st.info(question["question"])

        answer = st.text_area(
            "Your Answer",
            key="candidate_answer",
            height=180
        )

        if st.button(
            "Evaluate Answer",
            key="evaluate_answer"
        ):

            if len(answer.strip()) < 30:

                st.warning(
                    "Please write a more detailed answer."
                )

            else:

                result = evaluate_answer(
                    answer,
                    question["answer"]
                )

                st.metric(
                    "Interview Score",
                    f"{result['score']}%"
                )

                st.info(result["feedback"])

                if result["missing"]:

                    st.warning("Missing Keywords")

                    for word in result["missing"]:
                        st.write("•", word)

                with st.expander("Expected Answer"):
                    st.write(question["answer"])