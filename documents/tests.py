# from documents.pdf_utils import extract_text_from_pdf #, clean_text
# # text = extract_text_from_pdf("pdfs/Python_Project.pdf")
# # cleaned_text = clean_text(text)
# # print(cleaned_text[:1000])


from documents.pdf_utils import extract_pages_from_pdf

pages = extract_pages_from_pdf("pdfs/Python_Project.pdf")

for page in pages:
    print(f"\n--- Page {page['page_number']} ---")
    print(page['text'][:500])