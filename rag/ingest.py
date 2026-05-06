from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Load your dataset
loader = TextLoader("data/HR policy dataset.md")
documents = loader.load()

# 2. Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# 3. Create embeddings (Ollama)
embeddings = OllamaEmbeddings(model="llama3")

# 4. Store in Chroma DB
vectorstore = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="rag/vectordb"
)

vectorstore.persist()

print("✅ Ingestion complete. Vector DB created.")