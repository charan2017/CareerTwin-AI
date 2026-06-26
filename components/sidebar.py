import streamlit as st

def sidebar():

    st.sidebar.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=70
    )

    st.sidebar.title("CareerTwin AI")

    st.sidebar.caption(
        "AI Resume Intelligence Platform"
    )

    st.sidebar.divider()

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📄 Resume Analyzer",
            "📊 ATS Score",
            "🧠 Skill Gap",
            "🗺 Learning Roadmap",
            "💼 Career Advisor",
            "📈 Analytics",
            "⚙ Settings"
        ]
    )

    st.sidebar.divider()

    st.sidebar.success("Version 2.0")

    return page