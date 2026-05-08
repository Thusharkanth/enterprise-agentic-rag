from langchain_text_splitters import RecursiveCharacterTextSplitter


CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def split_documents(documents):
    """
    Split documents into smaller chunks for embedding.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )

    chunks = text_splitter.split_documents(documents)

    print(f"\nCreated {len(chunks)} chunks.\n")

    return chunks


if __name__ == "__main__":
    from loader import load_documents

    docs = load_documents()

    chunks = split_documents(docs)

    print("===== SAMPLE CHUNK =====\n")
    print(chunks[0].page_content)

    print("\n===== METADATA =====\n")
    print(chunks[0].metadata)