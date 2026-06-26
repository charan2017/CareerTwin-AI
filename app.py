import streamlit as st

from components.sidebar import sidebar
from components.dashboard import dashboard

st.set_page_config(
    page_title="CareerTwin AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

page = sidebar()

if page == "🏠 Dashboard":

    dashboard()

else:

    st.title(page)

    st.info("🚧 Module Under Development")