# Enterprise Agentic RAG Knowledge Assistant

An enterprise-grade Agentic RAG system built with LangGraph, ChromaDB, Google Gemini, and Ollama embeddings for intelligent internal knowledge retrieval.

## Project Overview

Enterprise teams often store critical knowledge across HR policies, onboarding guides, IT procedures, cybersecurity documents, AI governance rules, deployment standards, and support workflows. Finding the right answer manually is slow, repetitive, and difficult to audit.

This project solves that problem by providing a grounded AI assistant that retrieves relevant internal documents, evaluates whether the retrieved context is sufficient, and generates answers with source citations.

The system is designed to reduce hallucinated responses, improve knowledge accessibility, and make enterprise AI responses more explainable and traceable.

## Challenges This System Addresses

- LLMs without access to internal documents can produce hallucinated or unsupported answers.
- Ungrounded AI-generated responses create compliance, audit, and trust risks.
- Repetitive HR, IT, onboarding, policy, and process questions increase support workload.
- Enterprise knowledge is often scattered across multiple documents, making answers hard to find manually.
- Standard LLM responses lack source traceability and explainability.

## Features

- Agentic RAG workflow using LangGraph
- Semantic document retrieval with ChromaDB
- Local embedding generation using Ollama
- Gemini-powered grounded answer generation
- LLM-based context sufficiency evaluation
- Source citation support using document metadata
- Streamlit frontend for interactive querying
- Enterprise document ingestion pipeline
- Persistent local vector database
- Modular agent, service, graph, and ingestion layers

## System Architecture

![Architecture](diagrams/architecture.png)

The system is organized into four main layers:

| Layer | Responsibility |
|---|---|
| UI Layer | Streamlit interface for user queries and answer display |
| Orchestration Layer | LangGraph workflow that controls retrieve, evaluate, generate, and fallback routing |
| Retrieval Layer | ChromaDB similarity search over embedded enterprise documents |
| AI Layer | Gemini for context evaluation and grounded response generation |

## Agentic Workflow

![Workflow](diagrams/workflow.png)

```text
User Query
    |
    v
Retriever Agent
    |
    v
Evaluator Agent
    |
    +-- sufficient --> Answer Generator Agent
    |
    +-- insufficient --> Fallback Response
```

The current graph flow is:

```text
retrieve -> evaluate -> generate/fallback
```

### Workflow Steps

1. The user submits a question through the Streamlit application.
2. The retriever agent performs semantic search against ChromaDB.
3. The evaluator agent checks whether the retrieved context is enough to answer the question.
4. If the context is sufficient, the answer generator creates a grounded response.
5. If the context is insufficient, the system returns a controlled fallback message.
6. The final answer includes source filenames for traceability.

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| Workflow Engine | LangGraph |
| LLM | Google Gemini via `langchain-google-genai` |
| Embeddings | Ollama `nomic-embed-text` |
| Vector Database | ChromaDB |
| AI Framework | LangChain |
| Document Loading | LangChain Community Document Loaders |
| Text Splitting | RecursiveCharacterTextSplitter |
| Environment Management | python-dotenv |

## Repository Structure

```text
enterprise-agentic-rag/
|-- app.py
|-- agents/
|   |-- answer_generator.py
|   |-- evaluator_agent.py
|   |-- retriever_agent.py
|   |-- query_analyzer.py
|   `-- web_search_agent.py
|-- data/
|   `-- raw/
|-- diagrams/
|   |-- architecture.png
|   |-- rag_pipeline.png
|   `-- workflow.png
|-- docs/
|-- graph/
|   |-- nodes.py
|   |-- state.py
|   `-- workflow.py
|-- ingestion/
|   |-- chunker.py
|   |-- ingest.py
|   `-- loader.py
|-- prompts/
|   |-- analyzer_prompt.txt
|   |-- evaluator_prompt.txt
|   `-- generator_prompt.txt
|-- services/
|   |-- embeddings.py
|   |-- llm.py
|   `-- retrieval.py
|-- test/
|-- utils/
|-- vectorstore/
|   |-- chroma_db/
|   `-- vectordb.py
|-- requirements.txt
`-- README.md
```

## Installation Guide

### 1. Clone the Repository

```bash
git clone <repo-link>
cd enterprise-agentic-rag
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not populated yet, install the expected dependencies manually:

```bash
pip install streamlit python-dotenv langgraph langchain langchain-community langchain-text-splitters langchain-chroma langchain-ollama langchain-google-genai chromadb
```

## Ollama Setup

This project uses Ollama for local embedding generation.

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

The embedding model used by the application is configured in `services/embeddings.py`:

```python
EMBED_MODEL = "nomic-embed-text:latest"
```

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

The Gemini client is initialized in `services/llm.py`.

## Data Ingestion

Place enterprise knowledge documents in:

```text
data/raw/
```

The current implementation loads `.txt` files from this directory.

Run the ingestion pipeline:

```bash
python -m ingestion.ingest
```

The ingestion pipeline:

1. Loads text documents from `data/raw`.
2. Splits documents into overlapping chunks.
3. Generates embeddings with Ollama.
4. Stores vectors in ChromaDB under `vectorstore/chroma_db`.

Current chunking configuration:

| Setting | Value |
|---|---:|
| Chunk size | 500 |
| Chunk overlap | 100 |

## Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Example Queries

- How should employees report incidents?
- What are the cybersecurity guidelines?
- Explain the AI governance policy.
- What is the employee leave policy?
- What is the deployment approval process?
- What is the P1 SLA for enterprise clients?
- What AI tools are approved for employee use?

## Example Output

```text
Employees should report security incidents immediately through the approved reporting channels defined in the incident management workflow. The process includes notifying the security team, providing relevant incident details, and following escalation procedures based on severity.

Sources:
- 06_cybersecurity_guidelines.txt
- 09_incident_management_workflow.txt
```

## RAG Pipeline

![RAG Pipeline](diagrams/rag_pipeline.png)

The RAG pipeline has two major phases:

| Phase | Description |
|---|---|
| Ingestion | Loads, chunks, embeds, and stores enterprise documents in ChromaDB |
| Query Runtime | Retrieves relevant chunks, evaluates context, and generates grounded answers |

## Current Implementation Details

- The Streamlit app imports the compiled LangGraph workflow from `graph/workflow.py`.
- `graph/state.py` defines the shared graph state.
- `graph/nodes.py` maps workflow nodes to agent functions.
- `services/retrieval.py` performs similarity search with `k=4`.
- `agents/evaluator_agent.py` uses an LLM prompt that returns only `sufficient` or `insufficient`.
- `agents/answer_generator.py` builds the final grounded answer and appends source filenames.

## Current Limitations

- No user authentication or role-based access control.
- No hybrid search; retrieval is currently vector similarity only.
- No conversation memory across turns.
- No document upload or re-indexing from the UI.
- No cloud deployment configuration.
- No observability dashboard for latency, token usage, retrieval quality, or graph decisions.
- Source citations are filename-level, not exact section-level or line-level citations.
- The answer generator currently performs a second retrieval instead of reusing the context already stored in the graph state.
- Some files are placeholders for future capabilities, including query analysis and web search.

## Future Improvements

- Add hybrid retrieval with keyword search and vector search.
- Add query rewriting before retrieval.
- Add web search fallback for approved external sources.
- Add multi-agent collaboration for complex queries.
- Add role-based access control for enterprise users.
- Add document upload and re-indexing from the UI.
- Add chunk-level citations with section references.
- Add tracing and observability for retrieval, evaluation, and generation.
- Add automated tests for ingestion, retrieval, graph routing, and answer generation.
- Add deployment configuration for Docker or cloud platforms.

## Key Commands

```bash
# Build or rebuild the vector database
python -m ingestion.ingest

# Run the Streamlit application
streamlit run app.py

# Test retrieval manually
python -m services.retrieval

# Test the LangGraph workflow manually
python -m graph.workflow
```

## Author

Thusharkanth Loganathan  
AI/ML Engineer Intern

## License

This project is intended for educational and internal enterprise AI demonstration purposes. Update this section with the appropriate license before public release.

## Acknowledgements

- LangChain
- LangGraph
- Google Gemini
- Ollama
- ChromaDB
- Streamlit
