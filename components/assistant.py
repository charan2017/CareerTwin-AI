import streamlit as st


def show_ai_assistant(analysis):

    score = analysis["score"]

    if score >= 85:

        message = """
🎉 Excellent Resume!

You are almost job-ready.

Focus on:

• Interview Preparation

• Advanced Projects

• System Design

• GitHub Portfolio
"""

    elif score >= 70:

        message = """
👍 Good Progress!

Improve your profile by:

• Learning missing skills

• Building portfolio projects

• Practicing coding interviews
"""

    else:

        message = """
🚀 Keep Improving!

Recommended Next Steps:

• Learn core technical skills

• Complete certifications

• Build beginner projects

• Practice daily
"""

    strongest = "None"

    if analysis["matched"]:
        strongest = analysis["matched"][0]

    weakest = "None"

    if analysis["missing"]:
        weakest = analysis["missing"][0]

    st.markdown("## 🤖 AI Career Coach")

    st.info(message)

    c1, c2 = st.columns(2)

    with c1:

        st.success(f"💪 Strongest Skill\n\n{strongest}")

    with c2:

        st.warning(f"📚 Learn Next\n\n{weakest}")