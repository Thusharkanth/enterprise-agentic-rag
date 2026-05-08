from langchain_chroma import Chroma


PERSIST_DIRECTORY = "vectorstore/chroma_db"


def create_vector_store(chunks, embedding_model):
    """
    Create and persist Chroma vector database.
    """

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=PERSIST_DIRECTORY
    )

    print("\nChromaDB created successfully.\n")

    return vectorstore


def load_vector_store(embedding_model):
    """
    Load existing ChromaDB.
    """

    vectorstore = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_model
    )

    return vectorstore