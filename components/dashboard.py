import streamlit as st

def dashboard():

    st.title("🤖 CareerTwin AI")

    st.caption(
        "AI Powered Resume Intelligence Platform"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Resume Score", "--")

    with col2:
        st.metric("Skills", "--")

    with col3:
        st.metric("Missing", "--")

    with col4:
        st.metric("Job Ready", "--")

    st.divider()

    left, right = st.columns([2,1])

    with left:

        st.subheader("📄 Upload Resume")

        st.file_uploader(
            "Upload PDF Resume",
            type=["pdf"]
        )

    with right:

        st.subheader("Today's Goal")

        st.success("Upload Resume")

        st.info("Analyze Skills")

        st.warning("Improve ATS")

        st.error("Become Job Ready")