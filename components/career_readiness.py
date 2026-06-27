import streamlit as st


def show_career_readiness(data):

    st.divider()

    st.subheader("🚀 Career Readiness")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Resume",
            f"{data['resume']}%"
        )

    with c2:
        st.metric(
            "Job Match",
            f"{data['job_match']}%"
        )

    with c3:
        st.metric(
            "Skills",
            f"{data['skills']}%"
        )

    with c4:
        st.metric(
            "Overall",
            f"{data['overall']}%"
        )

    st.progress(
        data["overall"] / 100
    )

    st.success(data["status"])