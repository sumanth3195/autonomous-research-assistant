import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def format_report(state):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    # Build real references section
    references = ""
    for i, url in enumerate(state.web_sources, start=1):
        references += f"[{i}] {url}\n"

    prompt = f"""
    Convert the following research content into a structured markdown report.

    Structure:

    # Title
    ## Overview
    ## Key Concepts
    ## Applications
    ## Challenges
    ## Conclusion

    Do NOT invent references.
    Keep citation numbers already present.
    At the end, create a References section using ONLY these URLs:

    {references}

    Content:
    {state.verified_answer}
    """

    response = llm.invoke(prompt)

    state.final_answer = response.content
    return state









# def format_report(state):
#     llm = ChatGroq(
#         groq_api_key=os.getenv("GROQ_API_KEY"),
#         model_name="llama-3.1-8b-instant",
#         temperature=0
#     )

#     prompt = f"""
#     Convert the following research content into a structured markdown report.

#     Structure:

#     # Title
#     ## Overview
#     ## Key Concepts
#     ## Applications
#     ## Challenges
#     ## Conclusion
#     ## References

#     Content:
#     {state.draft_answer}
#     """

#     response = llm.invoke(prompt)
#     # try:
#     #     response = llm.invoke(prompt)
#     # except Exception as e:
#     #     print("Groq error in refine:", e)
#     #     state.refined_query = state.query
#     #     return state

#     state.final_answer = response.content
#     return state