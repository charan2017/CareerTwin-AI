import streamlit as st


def color(score):

    if score >= 80:
        return "🟢"

    if score >= 60:
        return "🟡"

    return "🔴"


def show_job_matches(results):

    st.divider()

    st.subheader("🎯 Job Match Analysis")

    for item in results:

        emoji = color(item["score"])

        st.progress(item["score"] / 100)

        st.markdown(
            f"""
**{emoji} {item['role']}**

Match Score: **{item['score']}%**
"""
        )