# 🤖 RoboTech Egypt - Enterprise RAG Support Assistant

An end-to-end, production-ready Retrieval-Augmented Generation (RAG) system built for automated customer support and internal knowledge retrieval.

## 🏗️ System Architecture & Tech Stack
* **Orchestration:** LangChain (LCEL)
* **Embedding Model:** `all-MiniLM-L6-v2` (Local HuggingFace embeddings, 100% offline & free)
* **Vector Database:** ChromaDB (Persistent local storage with metadata filtering)
* **LLM Generation:** Llama 3 (`openai/gpt-oss-20b` / Groq API for ultra-fast inference)
* **Frontend UI:** Streamlit

## 📁 Project Structure
```text
robotech-rag-assistant/
│
├── data/
│   └── raw/                  # Raw company policies (.md), product catalogs (.json), and FAQs (.txt)
├── vector_db/                # Persistent local ChromaDB vector store
├── src/                      
│   ├── ingest.py             # Format-aware custom document chunking & metadata tagging
│   ├── vector_store.py       # Local HuggingFace embedding pipeline & ChromaDB manager
│   ├── retriever.py          # LCEL RAG chain with anti-hallucination guardrails & source citation
│   └── app.py                # Streamlit interactive chat interface
│
├── .env                      # API keys (git-ignored)
├── .gitignore                
├── requirements.txt          # Project dependencies
└── README.md