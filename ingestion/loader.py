from langchain_community.document_loaders import DirectoryLoader, TextLoader

DATA_PATH = "data/raw"


def load_documents():
    """
    Load all TXT documents from the data/raw directory.
    """

    loader = DirectoryLoader(
        DATA_PATH,
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True
    )

    documents = loader.load()

    print(f"\nLoaded {len(documents)} text documents.\n")

    return documents


if __name__ == "__main__":
    docs = load_documents()

    # Preview first document
    print("===== SAMPLE DOCUMENT =====\n")
    print(docs[0].page_content[:500])

    print("\n===== METADATA =====\n")
    print(docs[0].metadata)