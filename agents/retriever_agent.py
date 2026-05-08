from services.retrieval import retrieve_documents


def retrieve_context(query):

    docs = retrieve_documents(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return docs, context