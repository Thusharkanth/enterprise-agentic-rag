from rag.retriever import get_retriever

retriever = get_retriever()

query = "What is sick leave policy?"

docs = retriever.get_relevant_documents(query)

for i, doc in enumerate(docs):
    print(f"\n--- Doc {i+1} ---")
    print(doc.page_content)