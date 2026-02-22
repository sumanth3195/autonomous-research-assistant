import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def web_search(state):
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    query_to_use = state.refined_query if state.refined_query else state.query

    # 🔥 FIX: Trim query to 350 characters (safe margin)
    safe_query = query_to_use[:350]

    results = client.search(safe_query, max_results=3)

    #state.web_results = [r["content"] for r in results["results"]]
    state.web_results = [r["content"] for r in results["results"]]
    state.web_sources = [r["url"] for r in results["results"]]

    return state