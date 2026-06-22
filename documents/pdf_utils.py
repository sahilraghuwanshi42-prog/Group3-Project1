import fitz
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf = fitz.open(pdf_path)
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
