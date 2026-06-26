import streamlit as st


def show_recommendations(data):

    st.subheader("🤖 AI Resume Suggestions")

    st.metric(
        "Estimated ATS After Improvements",
        f"{data['estimated_score']}%"
    )

    st.markdown("### 📌 Recommended Improvements")

    for item in data["suggestions"]:

        st.success(item)

    st.markdown("### 🚀 Recommended Project")

    st.info(data["project"])