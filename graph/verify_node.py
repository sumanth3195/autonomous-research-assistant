import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def verify(state):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    # Combine all source context
    source_context = "\n".join(state.retrieved_docs + state.web_results)

    prompt = f"""
You are a citation verification system.

Given:
1. Research draft
2. Source materials

Remove any claims not supported by the sources.
Keep only supported statements.
Do NOT add new information.

Sources:
{source_context}

Draft:
{state.draft_answer}

Return cleaned version only.
"""

    response = llm.invoke(prompt)

    state.verified_answer = response.content
    return state