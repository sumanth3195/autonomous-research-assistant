from services.llm import get_llm

def refine_query(state):
    llm = get_llm()

    response = llm.invoke(
        f"Improve and clarify this research query: {state.query}"
    )

    state.refined_query = response.content
    return state