from .loader import load_documents
from .chunker import split_documents

from services.embeddings import get_embedding_model
from vectorstore.vectordb import create_vector_store


def main():

    print("\n========== INGESTION PIPELINE STARTED ==========\n")

    # STEP 1 — Load Documents
    print("Loading documents...")
    documents = load_documents()

    # STEP 2 — Split Documents
    print("Splitting documents into chunks...")
    chunks = split_documents(documents)

    # STEP 3 — Initialize Embeddings
    print("Initializing embedding model...")
    embedding_model = get_embedding_model()

    # STEP 4 — Create Vector Store
    print("Creating ChromaDB vector store...")
    create_vector_store(chunks, embedding_model)

    print("\n========== INGESTION COMPLETED ==========\n")


if __name__ == "__main__":
    main()