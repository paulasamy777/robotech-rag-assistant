import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from ingest import load_and_chunk_data

load_dotenv()

# Define the local directory where ChromaDB will save vectors
PERSIST_DIRECTORY = "vector_db"

def get_vector_store():
    print("Initializing local HuggingFace embedding model...")
    
    # We use a lightweight, powerful open-source embedding model from HuggingFace
    # Runs 100% locally on your CPU/GPU for free, requiring no API key!
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Check if vector store already exists on disk
    if os.path.exists(PERSIST_DIRECTORY) and os.listdir(PERSIST_DIRECTORY):
        print("Loading existing Chroma vector store from disk...")
        vector_store = Chroma(
            persist_directory=PERSIST_DIRECTORY,
            embedding_function=embeddings
        )
    else:
        print("Building new Chroma vector store from ingested documents...")
        # 1. Load chunks from our ingest.py module
        docs = load_and_chunk_data()
        
        # 2. Create Chroma vector database and persist it locally
        vector_store = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=PERSIST_DIRECTORY
        )
        print(f"Successfully embedded and saved {len(docs)} chunks to ChromaDB!")

    return vector_store

if __name__ == "__main__":
    db = get_vector_store()
    print("\n--- Vector Store Test: Similarity Search ---")
    
    # Let's test a quick semantic search query!
    query = "How much is shipping to Alexandria?"
    results = db.similarity_search(query, k=2)
    
    print(f"Query: '{query}'\n")
    for i, doc in enumerate(results):
        print(f"Result {i+1} (Source: {doc.metadata.get('source')}):")
        print(f"{doc.page_content}\n")
        