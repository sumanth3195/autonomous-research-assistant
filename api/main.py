from fastapi import FastAPI
from pydantic import BaseModel
from graph.workflow import app as graph_app
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(title="Autonomous Research Assistant")

api.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    query: str

@api.post("/research")
async def research(request: ResearchRequest):
    result = graph_app.invoke({"query": request.query})

    return {
        "query": request.query,
        "report": result["final_answer"],
        "sources": result.get("web_sources", [])
    }






# from fastapi import FastAPI
# from pydantic import BaseModel
# from graph.workflow import app
# from fastapi.middleware.cors import CORSMiddleware
# api = FastAPI()
# api.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://autonomous-research-assistant-5j689zjkvqtp4lgdlarquu.streamlit.app/"],  # allow all for now
#     allow_credentials=True,
#     allow_methods=["https://autonomous-research-assistant-5j689zjkvqtp4lgdlarquu.streamlit.app/"],
#     allow_headers=["https://autonomous-research-assistant-5j689zjkvqtp4lgdlarquu.streamlit.app/"],
# )
# api = FastAPI(title="Autonomous Research Assistant")

# class ResearchRequest(BaseModel):
#     query: str

# @api.post("/research")
# async def research(request: ResearchRequest):
#     result = app.invoke({"query": request.query})

#     return {
#         "query": request.query,
#         "report": result["final_answer"],
#         "sources": result.get("web_sources", [])
#     }


