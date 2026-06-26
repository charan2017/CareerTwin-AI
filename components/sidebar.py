import streamlit as st


def sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h1 style='text-align:center;color:#60A5FA;'>
                🤖 CareerTwin AI
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align:center;color:gray;'>AI Resume Intelligence Platform</p>",
            unsafe_allow_html=True,
        )

        st.divider()

        page = st.radio(
            "📌 Navigation",
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

        st.divider()

        st.subheader("👨‍💻 Developer")

        st.write("**Charan Gosala**")

        st.caption("B.Tech AIML Student")

        st.divider()

        st.subheader("📊 Project Status")

        st.progress(0.35)

        st.caption("Sprint 4 in Progress")

        st.divider()

        st.info(
            """
### 🚀 CareerTwin AI Pro

Version **2.0**

AI Resume Intelligence Platform

Made with ❤️ using

- Python
- Streamlit
- Plotly
"""
        )

        st.divider()

        st.caption("© 2026 Charan Gosala")

    return page