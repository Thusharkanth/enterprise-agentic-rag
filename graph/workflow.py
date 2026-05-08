from langgraph.graph import StateGraph, END

from graph.state import GraphState

from graph.nodes import (
    retrieve_node,
    evaluate_node,
    generate_node,
    fallback_node
)


# Create graph
workflow = StateGraph(GraphState)


# Add nodes
workflow.add_node("retrieve", retrieve_node)

workflow.add_node("evaluate", evaluate_node)

workflow.add_node("generate", generate_node)

workflow.add_node("fallback", fallback_node)


# Entry point
workflow.set_entry_point("retrieve")


# Flow edges
workflow.add_edge("retrieve", "evaluate")


# Conditional routing
def route_decision(state):

    if state["evaluation"] == "sufficient":

        return "generate"

    return "fallback"


workflow.add_conditional_edges(
    "evaluate",
    route_decision,
    {
        "generate": "generate",
        "fallback": "fallback"
    }
)


# End nodes
workflow.add_edge("generate", END)

workflow.add_edge("fallback", END)


# Compile graph
app = workflow.compile()


if __name__ == "__main__":

    query = "How should employees report incidents?"

    result = app.invoke({
        "query": query
    })

    print("\n========== FINAL RESPONSE ==========\n")

    print(result["final_answer"])