
from langgraph.graph import StateGraph
from graph.state import ResearchState
from graph.refine_node import refine
from graph.web_node import web_search
from graph.retrieve_node import retrieve
from graph.generate_node import generate
from graph.verify_node import verify
from graph.format_node import format_report

workflow = StateGraph(ResearchState)

workflow.add_node("refine", refine)
workflow.add_node("web_search", web_search)
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("verify", verify)
workflow.add_node("format", format_report)

workflow.set_entry_point("refine")

workflow.add_edge("refine", "web_search")
workflow.add_edge("web_search", "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "verify")
workflow.add_edge("verify", "format")

app = workflow.compile()