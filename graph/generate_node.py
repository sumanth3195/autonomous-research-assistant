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
    # # Combine context
    # combined_docs = state.retrieved_docs + state.web_results

    # # Number the sources
    # numbered_context = ""
    # for i, doc in enumerate(combined_docs, start=1):
    #     numbered_context += f"[{i}] {doc}\n\n"

    # prompt = f"""
    # Answer the question using the sources below.

    # Cite using [number] format.

    # Sources:
    # {numbered_context}

    # Question:
    # {state.query}
    # """
    # #context = "\n".join(state.retrieved_docs)
    # context = "\n".join(state.retrieved_docs + state.web_results)

    # prompt = f"""
    # Answer ONLY using the context below.

    # Context:
    # {context}

    # Question:
    # {state.query}
    # """

    # Combine context
    # combined_docs = state.retrieved_docs + state.web_results

    # numbered_context = ""
    # for i, doc in enumerate(combined_docs, start=1):
    #     numbered_context += f"[{i}] {doc}\n\n"

    # prompt = f"""
    # You are a research assistant.

    # Generate a structured markdown research report.

    # Structure:

    # # Title

    # ## Overview
    # ## Key Concepts
    # ## Applications
    # ## Challenges
    # ## Conclusion
    # ## References

    # Use citation format [number] inside text.
    # Only use the provided sources.

    # Sources:
    # {numbered_context}

    # Question:
    # {state.query}
    # """
    # combined_docs = state.retrieved_docs + state.web_results
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
    # try:
    #     response = llm.invoke(prompt)
    # except Exception as e:
    #     print("Groq error in generate:", e)
    #     state.refined_query = state.query
    #     return state

    # state.final_answer = response.content
    # return state
    state.draft_answer = response.content
    return state

