import fitz
from langchain.docstore.document import Document

def extract_pdf(path):
    doc = fitz.open(path)
    documents = []

    for page in doc:
        text = page.get_text()
        documents.append(Document(page_content=text))

    return documents