import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def refine(state):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = f"""
    You are an AI research assistant.

    If the query contains ambiguous acronyms,
    expand them based on AI/technology context unless specified otherwise.

    Make the query specific and technical.

    User Query:
    {state.query}
    """

    response = llm.invoke(prompt)
    # try:
    #     response = llm.invoke(prompt)
    # except Exception as e:
    #     print("Groq error in refine:", e)
    #     state.refined_query = state.query
    #     return state

    state.refined_query = response.content
    return state