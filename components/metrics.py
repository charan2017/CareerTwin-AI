import streamlit as st


def show_metrics(score, matched, missing, readiness):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📊 Resume Score",
            value=f"{score}%"
        )

    with col2:
        st.metric(
            label="✅ Skills Found",
            value=len(matched)
        )

    with col3:
        st.metric(
            label="📚 Missing Skills",
            value=len(missing)
        )

    with col4:
        st.metric(
            label="🚀 Career Status",
            value=readiness
        )