import streamlit as st
import matplotlib.pyplot as plt

from resume_parser import extract_text
from skills_db import AI_ENGINEER

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="CareerTwin AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("🤖 CareerTwin AI")
st.write("Upload your resume and analyze your AI Engineer readiness.")

# -----------------------------
# Upload Resume
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# -----------------------------
# Process Resume
# -----------------------------

if uploaded_file:

    st.success("Resume Uploaded Successfully!")

    # Extract text
    resume_text = extract_text(uploaded_file)

    # Show resume text
    st.subheader("📄 Resume Text")

    st.text_area(
        "Extracted Content",
        resume_text,
        height=250
    )

    # -----------------------------
    # Detect Skills
    # -----------------------------

    detected_skills = []

    for skill in AI_ENGINEER:
        if skill.lower() in resume_text:
            detected_skills.append(skill)

    st.subheader("✅ Detected Skills")

    if detected_skills:
        for skill in detected_skills:
            st.success(skill)
    else:
        st.warning("No skills detected")

    # -----------------------------
    # Missing Skills
    # -----------------------------

    missing_skills = []

    for skill in AI_ENGINEER:
        if skill.lower() not in resume_text:
            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.error(skill)

    # -----------------------------
    # Readiness Score
    # -----------------------------

    score = int(
        (len(detected_skills) / len(AI_ENGINEER)) * 100
    )

    st.subheader("📊 AI Engineer Readiness")

    st.progress(score)

    st.write(f"### {score}% Ready")

    # -----------------------------
    # Pie Chart
    # -----------------------------

    st.subheader("📈 Skills Analytics")

    labels = ["Detected Skills", "Missing Skills"]

    sizes = [
        len(detected_skills),
        len(missing_skills)
    ]

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title("Skills Distribution")

    st.pyplot(fig)

    # -----------------------------
    # Learning Roadmap
    # -----------------------------

    st.subheader("🚀 Personalized Learning Roadmap")

    if missing_skills:

        for i, skill in enumerate(missing_skills, start=1):

            st.info(
                f"Week {i}: Learn {skill}"
            )

    # -----------------------------
    # Career Status
    # -----------------------------

    st.subheader("🎯 Career Status")

    if score >= 80:
        st.success("🟢 Job Ready")

    elif score >= 60:
        st.warning("🟡 Almost Ready")

    else:
        st.error("🔴 Needs More Preparation")