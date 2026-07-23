import streamlit as st

from components.sidebar import sidebar
from components.hero import hero
from components.dashboard import dashboard
from styles.theme import apply_theme
from components.interview import show_interview

st.set_page_config(
    page_title="CareerTwin AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()

# =====================================
# Custom Theme
# =====================================

hide_style = """
<style>

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

# =====================================
# Sidebar
# =====================================

page = sidebar()

# =====================================
# Dashboard
# =====================================

if page == "🏠 Dashboard":

    hero()

    dashboard()

# =====================================
# Resume Analyzer
# =====================================

elif page == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")
    st.info("Coming Soon")

# =====================================
# ATS Score
# =====================================

elif page == "📊 ATS Score":

    st.title("📊 ATS Score")
    st.info("Coming Soon")

# =====================================
# Skill Gap
# =====================================

elif page == "🧠 Skill Gap":

    st.title("🧠 Skill Gap")
    st.info("Coming Soon")

# =====================================
# Learning Roadmap
# =====================================

elif page == "🗺 Learning Roadmap":

    st.title("🗺 Learning Roadmap")
    st.info("Coming Soon")

# =====================================
# Career Advisor
# =====================================

elif page == "💼 Career Advisor":

    st.title("💼 Career Advisor")
    st.info("Coming Soon")

# =====================================
# Analytics
# =====================================

elif page == "📈 Analytics":

    st.title("📈 Analytics")
    st.info("Coming Soon")

# =====================================
# Settings
# =====================================

elif page == "⚙ Settings":

    st.title("⚙ Settings")
    st.info("Coming Soon")
elif page == "🎤 Interview Simulator":

    st.title("🎤 AI Interview Simulator")

    show_interview()