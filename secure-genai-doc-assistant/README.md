# Secure GenAI Enterprise Document Assistant (RAG + Encryption + Semantic Search)

Enterprise-grade GenAI document assistant built using Python, Streamlit, Gemini API, FAISS, and LangChain.

## Features

- Secure PDF upload and encrypted storage
- Retrieval-Augmented Generation (RAG)
- Semantic search using FAISS vector database
- Multi-document processing
- Authentication system
- Activity logging and monitoring
- Dashboard analytics
- Chat history management
- Context-aware document Q&A

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- FAISS
- LangChain
- Fernet Encryption
- Sentence Transformers

## Architecture

PDF Upload → Encryption → Text Extraction → Chunking → FAISS Vector Store → Semantic Retrieval → Gemini → Response

## Installation

```bash
pip install -r requirements.txt
```

Run:

```bash
py -m streamlit run app.py
```

## Sample Use Cases

- Enterprise document search
- Policy document assistant
- Secure knowledge management
- Internal AI support assistant