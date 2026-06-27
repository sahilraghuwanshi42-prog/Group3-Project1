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

def extract_pages_from_pdf(pdf_path):
    pages = []

    pdf = fitz.open(pdf_path)

    for page_num, page in enumerate(pdf, start=1):
        pages.append({
            "page_number": page_num,
            "text": page.get_text()
        })

    pdf.close()

    return pages


def extract_clauses(text):
    clauses = []

    for line in text.split("\n"):
        line = line.strip()

        if line:
            clauses.append(line)

    return clauses