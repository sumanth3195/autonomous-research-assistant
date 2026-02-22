from services.embeddings import get_embeddings

emb = get_embeddings()
print(emb.embed_query("test query"))