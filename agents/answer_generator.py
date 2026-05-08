from services.retrieval import retrieve_documents
from services.llm import extract_text, get_llm


def generate_answer(query):
    """
    Generate grounded answer using retrieved context.
    """

    # STEP 1 — Retrieve relevant documents
    retrieved_docs = retrieve_documents(query)

    # STEP 2 — Combine retrieved context
    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    # STEP 3 — Create prompt
    prompt = f"""
You are an intelligent enterprise knowledge assistant.

Answer the user's question ONLY using the provided context.

If the answer is not found in the context, say:
"I could not find sufficient information in the knowledge base."

==================== CONTEXT ====================

{context}

=================================================

Question:
{query}

Answer:
"""

    # STEP 4 — Initialize Gemini
    llm = get_llm()

    # STEP 5 — Generate response
    response = llm.invoke(prompt)

    # STEP 6 — Return clean response
    return extract_text(response)


if __name__ == "__main__":

    query = "How should employees report security incidents?"

    answer = generate_answer(query)

    print("\n========== GENERATED ANSWER ==========\n")

    print(answer)
