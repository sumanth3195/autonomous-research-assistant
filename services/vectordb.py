from langchain_community.vectorstores import Chroma
from services.embeddings import get_embeddings

def create_vectorstore(documents):
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=get_embeddings(),
        persist_directory="./chroma_db"
    )
    vectordb.persist()
    return vectordb

_vectordb = None

def load_vectorstore():
    global _vectordb
    if _vectordb is None:
        _vectordb = Chroma(
            persist_directory="chroma_db",
            embedding_function=get_embeddings()
        )
    return _vectordb




# def load_vectorstore():
#     vectordb = Chroma(
#         persist_directory="./chroma_db",
#         embedding_function=get_embeddings()
#     )
#     return vectordb


