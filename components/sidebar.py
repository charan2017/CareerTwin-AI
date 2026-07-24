import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown(
            "<h2 style='color:#3B82F6'>🤖 CareerTwin AI</h2>",
            unsafe_allow_html=True,
        )
        page = st.radio(
            "Navigation",
            ["🏠 Dashboard"],
        )
    return page