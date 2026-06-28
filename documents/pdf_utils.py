import fitz
import re

import spacy
nlp = spacy.load("en_core_web_sm")


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



def categorize_clause(clause):
    doc = nlp(clause)

    text = clause.lower()

    if "payment" in text:
        return "Payment"

    elif "termination" in text or "terminate" in text or "terminated" in text:
        return "Termination"

    elif "confidential" in text:
        return "Confidentiality"

    elif "jurisdiction" in text:
        return "Jurisdiction"

    elif "governing law" in text:
        return "Governing Law"

    return "General"


def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON", "GPE"]:
            entities.append({
                "text": ent.text,
                "label": ent.label_
            })

    return entities


def detect_risk(clause):
    text = clause.lower()

    high_risk = [
        "penalty",
        "liability",
        "indemnify",
        "terminate immediately",
        "breach"
    ]

    medium_risk = [
        "confidential",
        "arbitration",
        "jurisdiction"
    ]

    for word in high_risk:
        if word in text:
            return "High"

    for word in medium_risk:
        if word in text:
            return "Medium"

    return "Low"