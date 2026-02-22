from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en"
        )
    return _embeddings