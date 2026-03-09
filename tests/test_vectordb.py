from services.vectordb import create_vectorstore

texts = [
    "LoRa is a low power wide area network technology.",
    "RAG stands for Retrieval Augmented Generation.",
    "LangGraph is used for multi-agent orchestration."
]

vectordb = create_vectorstore(texts)

results = vectordb.similarity_search("What is RAG?")

for doc in results:
    print(doc.page_content)