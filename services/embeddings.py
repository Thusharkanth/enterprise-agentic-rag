from langchain_ollama import OllamaEmbeddings


EMBED_MODEL = "nomic-embed-text:latest"


def get_embedding_model():
    """
    Initialize Ollama embedding model.
    """

    embeddings = OllamaEmbeddings(
        model=EMBED_MODEL
    )

    return embeddings


if __name__ == "__main__":

    embedding_model = get_embedding_model()

    sample_text = "How are security incidents escalated?"

    vector = embedding_model.embed_query(sample_text)

    print(f"\nEmbedding vector size: {len(vector)}")
    print("\nSample vector values:")
    print(vector[:10])