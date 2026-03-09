from graph.workflow import app

result = app.invoke({"query": "What is RAG?"})

print("---- FINAL ANSWER ----")
print(result["final_answer"])
print("\n---- WEB SOURCES ----")
for i, url in enumerate(result.get("web_sources", []), start=1):
    print(f"[{i}] {url}")