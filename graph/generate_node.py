import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def generate(state):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0
    )
  
    combined_docs = state.web_results

    numbered_context = ""
    for i, doc in enumerate(combined_docs, start=1):
        numbered_context += f"[{i}] {doc}\n\n"

    prompt = f"""
    Answer the question in detailed paragraph form.
    Use citation format [number].
    Do NOT format as markdown.
    Just provide raw research content.

    Sources:
    {numbered_context}

    Question:
    {state.query}
    """
    response = llm.invoke(prompt)
    
    state.draft_answer = response.content
    return state

