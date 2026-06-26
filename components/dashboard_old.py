import streamlit as st

from resume_parser import extract_text
from utils.extractor import extract_candidate_info
from utils.analyzer import analyze_resume
from skills_db import ROLES

from components.metrics import show_metrics
from components.gauge import show_gauge
from components.charts import show_dashboard
from components.candidate import show_candidate
from components.assistant import show_ai_assistant
from components.roadmap import show_roadmap

def dashboard():

    st.markdown("## 📄 Resume Analysis")

    upload_col, role_col = st.columns([2, 1])

    with upload_col:

        uploaded = st.file_uploader(
            "Upload Your Resume (PDF)",
            type=["pdf"],
            help="Upload a professional resume in PDF format."
        )

    with role_col:

        selected_role = st.selectbox(
            "🎯 Target Role",
            list(ROLES.keys())
        )

    st.divider()

    # -----------------------------
    # Wait for Resume Upload
    # -----------------------------

    if uploaded is None:

        st.info("👆 Upload your resume to begin analysis.")

        return

    # -----------------------------
    # Resume Processing
    # -----------------------------

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text(uploaded)

        info = extract_candidate_info(resume_text)

        analysis = analyze_resume(
            resume_text,
            selected_role
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

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Skills Found")

        if analysis["matched"]:

            for skill in analysis["matched"]:

                st.success(skill)

        else:

            st.warning("No matching skills found.")

    with right:

        st.subheader("❌ Missing Skills")

        if analysis["missing"]:

            for skill in analysis["missing"]:

                st.warning(skill)

        else:

            st.success("No missing skills 🎉")

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
    # Career Status
    # -----------------------------

    st.subheader("🎯 Career Status")

    if analysis["score"] >= 80:

        st.success(
            """
🎉 Excellent!

Your resume looks strong for the selected role.

### Next Steps
- Practice coding interviews
- Build 2–3 advanced projects
- Keep your GitHub updated
- Start applying for internships/jobs
"""
        )

    elif analysis["score"] >= 60:

        st.warning(
            """
👍 Good Progress!

You're close to being job-ready.

### Recommended Actions
- Learn the missing skills
- Improve your resume
- Build more portfolio projects
- Practice aptitude and interviews
"""
        )

    else:

        st.error(
            """
🚀 Keep Learning!

Your resume needs improvement.

### Focus On
- Learning the missing skills
- Completing certifications
- Building beginner projects
- Strengthening your fundamentals
"""
        )

    st.divider()

    # -----------------------------
    # Resume Preview
    # -----------------------------

    with st.expander("📄 Resume Preview"):

        st.text_area(
            "Extracted Resume Text",
            resume_text,
            height=350
        )

    st.divider()

    # -----------------------------
    # Footer
    # -----------------------------

    st.divider()

    show_roadmap(
        analysis
    )

    st.caption(
        "🤖 CareerTwin AI Pro • AI Career Intelligence Platform • Version 2.0"
    )