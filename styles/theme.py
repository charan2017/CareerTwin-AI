import streamlit as st


def apply_theme():

    st.markdown("""
<style>

/* ----------------------------------------------------
   Google Font
---------------------------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');


/* ----------------------------------------------------
   Global
---------------------------------------------------- */

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{

    background:#0B1120;

    color:white;
}

.block-container{

    max-width:1450px;

    padding-top:2rem;

    padding-bottom:2rem;
}


/* ----------------------------------------------------
   Sidebar
---------------------------------------------------- */

section[data-testid="stSidebar"]{

    background:#111827;

    border-right:1px solid #1F2937;
}


/* ----------------------------------------------------
   Metrics
---------------------------------------------------- */

div[data-testid="stMetric"]{

    background:#111827;

    border:1px solid #1F2937;

    border-radius:18px;

    padding:18px;

    transition:.25s;
}

div[data-testid="stMetric"]:hover{

    border:1px solid #3B82F6;

    transform:translateY(-2px);
}


/* ----------------------------------------------------
   Buttons
---------------------------------------------------- */

.stButton>button{

    width:100%;

    border:none;

    border-radius:12px;

    background:linear-gradient(90deg,#2563EB,#7C3AED);

    color:white;

    font-weight:600;

    padding:12px;

    transition:.25s;
}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:0 10px 20px rgba(59,130,246,.35);
}


/* ----------------------------------------------------
   File Uploader
---------------------------------------------------- */

[data-testid="stFileUploader"]{

    background:#111827;

    border:2px dashed #334155;

    border-radius:18px;

    padding:20px;
}


/* ----------------------------------------------------
   Select Box
---------------------------------------------------- */

[data-baseweb="select"]{

    border-radius:12px;
}


/* ----------------------------------------------------
   Progress
---------------------------------------------------- */

.stProgress>div>div{

    background:#2563EB;
}


/* ----------------------------------------------------
   Expander
---------------------------------------------------- */

details{

    background:#111827;

    border-radius:14px;

    border:1px solid #1F2937;

    padding:8px;
}


/* ----------------------------------------------------
   Divider
---------------------------------------------------- */

hr{

    border-color:#334155;
}


/* ----------------------------------------------------
   Success / Warning / Info
---------------------------------------------------- */

div[data-testid="stAlert"]{

    border-radius:14px;
}

</style>
""", unsafe_allow_html=True)