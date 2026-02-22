from services.vectordb import load_vectorstore

def retrieve(state):
    vectordb = load_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # docs = retriever.invoke(state.query)
    query_to_use = state.refined_query if state.refined_query else state.query
    docs = retriever.invoke(query_to_use)

    state.retrieved_docs = [doc.page_content for doc in docs]
    return state