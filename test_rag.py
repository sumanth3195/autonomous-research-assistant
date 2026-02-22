import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from services.vectordb import load_vectorstore

load_dotenv()

# Load LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# Load existing vector DB
vectordb = load_vectorstore()

# Create retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

query = "What is RAG?"

# Retrieve relevant documents
docs = retriever.invoke(query)
context = "\n".join([doc.page_content for doc in docs])

prompt = f"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

print("---- ANSWER ----")
print(response.content)