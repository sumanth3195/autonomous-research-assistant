from pydantic import BaseModel
from typing import List, Dict

class ResearchState(BaseModel):
    query: str
    refined_query: str = ""
    web_results: List[str] = []
    web_sources: List[str] = []
    retrieved_docs: List[str] = []
    draft_answer: str = ""   # NEW
    final_answer: str = ""
    verified_answer: str = ""