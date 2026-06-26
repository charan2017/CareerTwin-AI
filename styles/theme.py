import streamlit as st


def apply_theme():

    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

.stApp{
    background:#0F172A;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* Buttons */

.stButton>button{

    width:100%;
    border-radius:12px;
    border:none;
    background:linear-gradient(90deg,#4F46E5,#7C3AED);
    color:white;
    font-weight:bold;
    padding:12px;
}

/* File uploader */

[data-testid="stFileUploader"]{

    border:2px dashed #334155;
    border-radius:16px;
    padding:18px;
    background:#111827;
}

/* Selectbox */

[data-baseweb="select"]{

    border-radius:12px;
}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:#111827;
}

/* Divider */

hr{

    border-color:#334155;
}

</style>
""", unsafe_allow_html=True)