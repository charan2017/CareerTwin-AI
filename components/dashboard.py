import streamlit as st

from utils.job_match import calculate_job_matches
from components.job_match import show_job_matches
from utils.suggestions import generate_suggestions
from components.recommendations import show_recommendations
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
from utils.suggestions import generate_suggestions
from components.recommendations import show_recommendations


def dashboard():

    st.markdown("## 📄 Resume Analysis")

    col1, col2 = st.columns([2, 1])

    with col1:

        uploaded = st.file_uploader(
            "Upload Resume",
            type=["pdf"]
        )

    with col2:

        selected_role = st.selectbox(
            "🎯 Target Role",
            list(ROLES.keys())
        )

    st.divider()

    if uploaded is None:

        st.info("👆 Upload your resume to start analysis.")

        return

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text(uploaded)

        info = extract_candidate_info(
            resume_text
        )

        analysis = analyze_resume(
            resume_text,
            selected_role
        )

    st.success("✅ Resume analyzed successfully!")

    show_metrics(

        analysis["score"],

        analysis["matched"],

        analysis["missing"],

        analysis["readiness"]

    )

    st.divider()

    left, right = st.columns(2)

    with left:

        show_candidate(info)

    with right:

        st.subheader("📊 ATS Score")

        show_gauge(
            analysis["score"]
        )

    st.divider()
        # =====================================================
    # Skills Section
    # =====================================================

    skill_col1, skill_col2 = st.columns(2)

    with skill_col1:

        st.subheader("✅ Skills Found")

        if analysis["matched"]:

            for skill in analysis["matched"]:
                st.success(skill)

        else:

            st.warning("No matching skills found.")

    with skill_col2:

        st.subheader("❌ Missing Skills")

        if analysis["missing"]:

            for skill in analysis["missing"]:
                st.warning(skill)

        else:

            st.success("No missing skills!")

    st.divider()

    # =====================================================
    # Analytics Dashboard
    # =====================================================

    st.subheader("📈 Analytics Dashboard")

    show_dashboard(
        analysis
    )

    st.divider()

    # =====================================================
    # AI Career Coach
    # =====================================================

    # =====================================================
# AI Career Coach
# =====================================================

    show_ai_assistant(
        analysis
    )

# =====================================================
# AI Resume Suggestions
# =====================================================

    suggestion_data = generate_suggestions(
        analysis,
        selected_role
    )

    show_recommendations(
        suggestion_data
    )

    st.divider()
        # =====================================================
    # Career Status
    # =====================================================

    st.subheader("🎯 Career Status")

    score = analysis["score"]

    if score >= 80:

        st.success(
            """
🎉 Excellent!

Your resume is strong for the selected role.

### Recommended Next Steps
- Practice coding interviews
- Build advanced projects
- Keep GitHub updated
- Apply for internships/jobs
"""
        )

    elif score >= 60:

        st.warning(
            """
👍 Good Progress!

You are close to becoming job-ready.

### Recommended Actions
- Learn the missing skills
- Improve your resume
- Build more portfolio projects
- Practice aptitude & interviews
"""
        )

    else:

        st.error(
            """
🚀 Keep Improving!

Your resume still needs work.

### Focus On
- Learn the missing skills
- Complete certifications
- Build beginner projects
- Strengthen core concepts
"""
        )

    st.divider()

    # =====================================================
    # Learning Roadmap
    # =====================================================

    show_roadmap(
        analysis
    )

    st.divider()
        # =====================================================
    # Resume Preview
    # =====================================================

    with st.expander("📄 Resume Preview", expanded=False):

        st.text_area(
            "Extracted Resume Text",
            resume_text,
            height=350
        )

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.markdown(
        """
---
### 🤖 CareerTwin AI Pro

AI Career Intelligence Platform

**Developed by Charan Gosala**

Version **2.0**
"""
    )
    # =====================================================
# Job Match Analysis
# =====================================================

    job_matches = calculate_job_matches(
        resume_text
    )

    show_job_matches(
        job_matches
    )

    st.divider()