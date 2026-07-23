try:
    import pdfplumber
    print("pdfplumber imported successfully")
except Exception as e:
    raise Exception(f"IMPORT ERROR: {type(e).__name__}: {e}")
from PyPDF2 import PdfReader

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text.lower()