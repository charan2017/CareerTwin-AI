import streamlit as st

from components.sidebar import sidebar
from components.hero import hero
from components.dashboard import dashboard
from components.hero import hero

st.set_page_config(
    page_title="CareerTwin AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit default menu/footer
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="stMetric"]{
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
}

div[data-testid="stMetric"]:hover{
    border:1px solid #6366F1;
}

section[data-testid="stSidebar"]{
    background:#111827;
}
</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

page = sidebar()

if page == "🏠 Dashboard":


    hero()

    dashboard()

elif page == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")
    st.info("Coming in Sprint 5")

elif page == "📊 ATS Score":

    st.title("📊 ATS Score")
    st.info("Coming in Sprint 5")

elif page == "🧠 Skill Gap":

    st.title("🧠 Skill Gap")
    st.info("Coming in Sprint 6")

elif page == "🗺 Learning Roadmap":

    st.title("🗺 Learning Roadmap")
    st.info("Coming in Sprint 6")

elif page == "💼 Career Advisor":

    st.title("💼 Career Advisor")
    st.info("Coming in Sprint 7")

elif page == "📈 Analytics":

    st.title("📈 Analytics")
    st.info("Coming in Sprint 7")

elif page == "⚙ Settings":

    st.title("⚙ Settings")
    st.info("Coming in Sprint 8")