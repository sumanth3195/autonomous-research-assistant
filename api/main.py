from fastapi import FastAPI
from pydantic import BaseModel
from graph.workflow import app

api = FastAPI(title="Autonomous Research Assistant")

class ResearchRequest(BaseModel):
    query: str

@api.post("/research")
async def research(request: ResearchRequest):
    result = app.invoke({"query": request.query})

    return {
        "query": request.query,
        "report": result["final_answer"],
        "sources": result.get("web_sources", [])
    }