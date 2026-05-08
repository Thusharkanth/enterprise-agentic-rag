from services.retrieval import retrieve_documents
from agents.answer_generator import generate_answer

# NODE 1 — RETRIEVER NODE

def retrieve_node(state):

    query = state["query"]

    docs = retrieve_documents(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return {
        "retrieved_docs": docs,
        "context": context
    }

# NODE 2 — EVALUATOR NODE

def evaluate_node(state):

    context = state["context"]

    # Basic evaluation logic
    if len(context.strip()) < 50:

        evaluation = "insufficient"

    else:

        evaluation = "sufficient"

    return {
        "evaluation": evaluation
    }

# NODE 3 — ANSWER GENERATOR

def generate_node(state):

    query = state["query"]

    answer = generate_answer(query)

    return {
        "final_answer": answer
    }

#NODE 4 — FALLBACK NODE

def fallback_node(state):

    return {
        "final_answer":
        "I could not find sufficient information in the enterprise knowledge base."
    }