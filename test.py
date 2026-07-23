import streamlit as st
import pdfplumber
import sys

st.title("CareerTwin AI Test")

st.write("Python:", sys.version)
st.write("pdfplumber version:", pdfplumber.__version__)

st.success("✅ pdfplumber imported successfully")
