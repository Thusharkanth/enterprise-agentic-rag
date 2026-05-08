from agents.retriever_agent import retrieve_context

from agents.evaluator_agent import evaluate_context

from agents.answer_generator import generate_answer


def retrieve_node(state):

    query = state["query"]

    docs, context = retrieve_context(query)

    return {
        "retrieved_docs": docs,
        "context": context
    }


def evaluate_node(state):

    query = state["query"]

    context = state["context"]

    evaluation = evaluate_context(query, context)

    return {
        "evaluation": evaluation
    }


def generate_node(state):

    query = state["query"]

    answer = generate_answer(query)

    return {
        "final_answer": answer
    }


def fallback_node(state):

    return {
        "final_answer":
        "I could not find sufficient information in the enterprise knowledge base."
    }