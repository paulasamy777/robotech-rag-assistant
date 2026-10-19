import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from vector_store import get_vector_store

# Load environment variables (reads GROQ_API_KEY from .env)
load_dotenv()

def get_rag_chain():
    print("Connecting to Chroma vector store...")
    db = get_vector_store()
    
    # 1. Setup the Retriever
    # search_kwargs={"k": 3} means retrieve the top 3 most relevant chunks
    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    print("Initializing Groq LLM (Llama 3)...")
    # 2. Initialize the LLM via Groq API (Blazing fast & free)
    llm = ChatGroq(
        model="openai/gpt-oss-20b",  # <--- Active, high-speed production model on Groq
        temperature=0.1
    )

    # 3. Create a Strict Anti-Hallucination System Prompt
    system_prompt = (
        "You are an official customer support and technical assistant for RoboTech Egypt.\n"
        "Use the following retrieved context pieces to answer the user's question.\n"
        "If you do not know the answer or if it is not present in the provided context, "
        "politely state: 'I don't have that information in our official records. Please contact support at 19000.'\n"
        "Never make up prices, policies, or product specifications.\n"
        "Always cite the source file name (e.g., company_policies.md, products_catalog.json) when providing factual details.\n\n"
        "Context:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}")
    ])

    # Helper function to format retrieved documents into a single text block
    def format_docs(docs):
        formatted = []
        for doc in docs:
            source = doc.metadata.get("source", "unknown")
            formatted.append(f"\n{doc.page_content}")
        return "\n\n---\n\n".join(formatted)

    # 4. Build the LangChain Expression Language (LCEL) Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

if __name__ == "__main__":
    chain = get_rag_chain()
    
    print("\n--- RAG Engine Test ---")
    test_question = "How much is shipping to Alexandria if I want to buy an Arduino Mega?"
    print(f"User Question: {test_question}\n")
    
    # Run the chain
    response = chain.invoke(test_question)
    
    print("AI Assistant Response:")
    print(response)