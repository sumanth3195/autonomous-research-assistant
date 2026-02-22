from services.pdf_ingest import ingest_pdfs

vectordb = ingest_pdfs("data/pdfs")

print("PDFs ingested successfully.")