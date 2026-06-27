import os
import streamlit as st

from utils.pdf_report import generate_pdf


def show_pdf_download(info, analysis, suggestions):

    st.divider()

    st.subheader("📄 Career Report")

    output_file = "reports/Career_Report.pdf"

    if st.button(
        "📥 Generate Career Report",
        key="generate_pdf_button"
    ):

        os.makedirs("reports", exist_ok=True)

        generate_pdf(
            info,
            analysis,
            suggestions,
            output_file
        )

        st.success("✅ Career Report Generated!")

        with open(output_file, "rb") as pdf:

            st.download_button(
                label="⬇ Download Career Report",
                data=pdf,
                file_name="CareerTwin_AI_Report.pdf",
                mime="application/pdf",
                key="download_pdf_button"
            )