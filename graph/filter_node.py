# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# def filter_sources(state):
#     llm = ChatGroq(
#         groq_api_key=os.getenv("GROQ_API_KEY"),
#         model_name="llama-3.1-8b-instant",
#         temperature=0
#     )

#     filtered_results = []
#     filtered_urls = []

#     for content, url in zip(state.web_results, state.web_sources):
#         prompt = f"""
# Is this content highly relevant to the query below?
# Answer YES or NO only.

# Query:
# {state.query}

# Content:
# {content}
# """

#         response = llm.invoke(prompt)

#         if "YES" in response.content.upper():
#             filtered_results.append(content)
#             filtered_urls.append(url)

#     state.web_results = filtered_results
#     state.web_sources = filtered_urls

#     return state