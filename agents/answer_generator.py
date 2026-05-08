import os

from services.retrieval import retrieve_documents
from services.llm import get_llm


def generate_answer(query):
    """
    Generate grounded answer using retrieved context
    and append source citations.
    """

    # STEP 1 — Retrieve relevant documents
    retrieved_docs = retrieve_documents(query)

    # STEP 2 — Build context
    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    # STEP 3 — Extract source filenames
    sources = []

    for doc in retrieved_docs:

        source_path = doc.metadata.get("source", "Unknown Source")

        filename = os.path.basename(source_path)

        sources.append(filename)

    # Remove duplicates
    unique_sources = list(set(sources))

    # STEP 4 — Build prompt
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

    # STEP 5 — Initialize LLM
    llm = get_llm()

    # STEP 6 — Generate response
    response = llm.invoke(prompt)

    # STEP 7 — Clean response
    if hasattr(response, "content"):

        content = response.content

        if isinstance(content, list):

            answer = content[0]["text"]

        else:

            answer = str(content)

    else:

        answer = str(response)

    # STEP 8 — Append citations
    citations = "\n\nSources:\n"

    for source in unique_sources:

        citations += f"- {source}\n"

    final_answer = answer + citations

    return final_answer


if __name__ == "__main__":

    query = "How should employees report incidents?"

    answer = generate_answer(query)

    print("\n========== GENERATED ANSWER ==========\n")

    print(answer)