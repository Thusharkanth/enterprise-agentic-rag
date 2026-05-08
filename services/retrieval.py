from vectorstore.vectordb import load_vector_store
from services.embeddings import get_embedding_model


def retrieve_documents(query, k=4):
    """
    Retrieve relevant document chunks from ChromaDB.
    """

    # Load embedding model
    embedding_model = get_embedding_model()

    # Load vector database
    vectorstore = load_vector_store(embedding_model)

    # Perform similarity search
    results = vectorstore.similarity_search(
        query=query,
        k=k
    )

    return results


if __name__ == "__main__":

    query = "How are security incidents escalated?"

    results = retrieve_documents(query)

    print("\n========== RETRIEVAL RESULTS ==========\n")

    for i, doc in enumerate(results, start=1):

        print(f"\n--- Result {i} ---\n")

        print(doc.page_content[:500])

        print("\nMetadata:")
        print(doc.metadata)