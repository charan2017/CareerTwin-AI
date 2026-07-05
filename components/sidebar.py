import streamlit as st


def sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:10px;
            ">
                <h1 style="color:#3B82F6;margin-bottom:5px;">
                    🤖 CareerTwin AI
                </h1>

                <p style="
                    color:#94A3B8;
                    font-size:15px;
                ">
                    AI Career Intelligence Platform
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        page = st.radio(
            "📌 Navigation",
            [
                "🏠 Dashboard",
                "📄 Resume Analyzer",
                "📊 ATS Score",
                "🎯 Skill Gap",
                "🗺 Learning Roadmap",
                "💼 Career Advisor",
                "📈 Analytics",
                "⚙ Settings",
                "🎤 Interview Simulator",
            ],
            key="sidebar_navigation",
        )

        st.divider()

        st.markdown("### 👨‍💻 Developer")

        st.success("**Charan Gosala**")

        st.caption("B.Tech AI & ML Student")

        st.divider()

        st.markdown("### 🚀 Project Progress")

        st.progress(0.75)

        st.caption("Version 3.0 Development")

        st.divider()

        st.info(
            """
### 🌟 CareerTwin AI Pro

**Current Features**

- 📄 Resume Analysis
- 📊 ATS Score
- 🎯 Job Match
- 🚀 Career Readiness
- 🤖 AI Resume Coach
- 🗺 Learning Roadmap
- 📄 PDF Report
"""
        )

        st.divider()

        st.caption("© 2026 Charan Gosala")

    return page