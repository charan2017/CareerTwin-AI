import streamlit as st


def show_candidate(info):

    st.subheader("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("📧 Email")
        st.success(info["email"] or "Not Found")

        st.write("📱 Phone")
        st.success(info["phone"] or "Not Found")

    with col2:

        st.write("💻 GitHub")
        st.success(info["github"] or "Not Found")

        st.write("💼 LinkedIn")
        st.success(info["linkedin"] or "Not Found")