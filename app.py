import streamlit as st
import sys
import subprocess

st.title("CareerTwin AI - Debug")

st.write("Python Version:")
st.code(sys.version)

st.write("Checking pdfplumber...")

result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "pdfplumber"],
    capture_output=True,
    text=True,
)

st.code(result.stdout if result.stdout else result.stderr)

st.write("Installed packages containing 'pdf':")

result = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True,
    text=True,
)

packages = [
    line for line in result.stdout.splitlines()
    if "pdf" in line.lower()
]

st.code("\n".join(packages))

st.stop()
import streamlit as st

from components.sidebar import sidebar
from components.hero import hero
from components.dashboard import dashboard
from styles.theme import apply_theme
from components.interview import show_interview

st.set_page_config(
    
    apply_theme()
    page_title="CareerTwin AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

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