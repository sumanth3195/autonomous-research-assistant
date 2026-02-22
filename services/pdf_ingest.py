import fitz
import os
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.schema import Document
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from services.vectordb import create_vectorstore

def ingest_pdfs(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file)
            doc = fitz.open(pdf_path)

            full_text = ""
            for page in doc:
                full_text += page.get_text()

            documents.append(Document(
                page_content=full_text,
                metadata={"source": file}
            ))

    # 🔥 Chunking (Very Important)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    split_docs = splitter.split_documents(documents)

    # Store in vector DB
    vectordb = create_vectorstore(split_docs)

    return vectordb