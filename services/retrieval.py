from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def get_retriever():
    embeddings = OllamaEmbeddings(model="llama3")

    vectorstore = Chroma(
        persist_directory="rag/vectordb",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return retriever