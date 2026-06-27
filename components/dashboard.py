import streamlit as st

# -----------------------------
# Resume Processing
# -----------------------------
from resume_parser import extract_text
from utils.extractor import extract_candidate_info
from utils.analyzer import analyze_resume
from skills_db import ROLES

# -----------------------------
# Components
# -----------------------------
from components.metrics import show_metrics
from components.gauge import show_gauge
from components.charts import show_dashboard
from components.candidate import show_candidate
from components.assistant import show_ai_assistant
from components.roadmap import show_roadmap
from components.recommendations import show_recommendations
from components.job_match import show_job_matches
from components.pdf_download import show_pdf_download

# -----------------------------
# Utilities
# -----------------------------
from utils.suggestions import generate_suggestions
from utils.job_match import calculate_job_matches


def dashboard():

    st.markdown("## 📄 Resume Analysis")

    upload_col, role_col = st.columns([2, 1])

    with upload_col:

        uploaded = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"],
            help="Upload your resume in PDF format."
        )

    with role_col:

        selected_role = st.selectbox(
            "🎯 Target Role",
            list(ROLES.keys())
        )

    st.divider()

    if uploaded is None:

        st.info("👆 Upload your resume to begin analysis.")

        return

    # -----------------------------
    # Analyze Resume
    # -----------------------------

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text(uploaded)

        info = extract_candidate_info(
            resume_text
        )

        analysis = analyze_resume(
            resume_text,
            selected_role
        )

        suggestion_data = generate_suggestions(
            analysis,
            selected_role
        )

        job_matches = calculate_job_matches(
            resume_text
        )

    st.success("✅ Resume analyzed successfully!")

    # -----------------------------
    # KPI Cards
    # -----------------------------

    show_metrics(
        analysis["score"],
        analysis["matched"],
        analysis["missing"],
        analysis["readiness"]
    )

    st.divider()

    # -----------------------------
    # Candidate + ATS
    # -----------------------------

    left, right = st.columns(2)

    with left:

        show_candidate(info)

    with right:

        st.subheader("📊 ATS Score")

        show_gauge(
            analysis["score"]
        )

    st.divider()
        # -----------------------------
    # Skills Section
    # -----------------------------

    skills_col1, skills_col2 = st.columns(2)

    with skills_col1:

        st.subheader("✅ Skills Found")

        if analysis["matched"]:

            for skill in analysis["matched"]:
                st.success(skill)

        else:

            st.warning("No matching skills found.")

    with skills_col2:

        st.subheader("❌ Missing Skills")

        if analysis["missing"]:

            for skill in analysis["missing"]:
                st.warning(skill)

        else:

            st.success("No missing skills!")

    st.divider()

    # -----------------------------
    # Analytics Dashboard
    # -----------------------------

    st.subheader("📈 Analytics Dashboard")

    show_dashboard(
        analysis
    )

    st.divider()

    # -----------------------------
    # AI Career Coach
    # -----------------------------

    show_ai_assistant(
        analysis
    )

    st.divider()

    # -----------------------------
    # AI Resume Suggestions
    # -----------------------------

    show_recommendations(
        suggestion_data
    )

    st.divider()
        # -----------------------------
    # Job Match Analysis
    # -----------------------------

    show_job_matches(
        job_matches
    )

    st.divider()

    # -----------------------------
    # Learning Roadmap
    # -----------------------------

    st.subheader("🗺 Personalized Learning Roadmap")

    show_roadmap(
        analysis
    )

    st.divider()

    # -----------------------------
    # PDF Career Report
    # -----------------------------

    show_pdf_download(
        info,
        analysis,
        suggestion_data
    )

    st.divider()
        # -----------------------------
    # Job Match Analysis
    # -----------------------------

    show_job_matches(
        job_matches
    )

    st.divider()

    # -----------------------------
    # Learning Roadmap
    # -----------------------------

    st.subheader("🗺 Personalized Learning Roadmap")

    show_roadmap(
        analysis
    )

    st.divider()

    # -----------------------------
    # PDF Career Report
    # -----------------------------

   