import streamlit as st
from retriever import get_rag_chain

# Page Configuration
st.set_page_config(
    page_title="RoboTech Egypt Assistant",
    page_icon="🤖",
    layout="centered"
)

# App Header
st.title("🤖 RoboTech Egypt - AI Support Assistant")
st.markdown("Ask anything about our products, shipping policies, warranties, or FAQs!")

# Initialize RAG Chain (cached so it only loads once for performance)
@st.cache_resource
def load_chain():
    return get_rag_chain()

with st.spinner("Initializing RoboTech RAG Engine... Please wait."):
    rag_chain = load_chain()

# Maintain chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages on re-run
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box at the bottom
if prompt := st.chat_input("Type your question here (e.g., How much is shipping to Cairo?)"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response using our RAG chain
    with st.chat_message("assistant"):
        with st.spinner("Thinking... searching company knowledge base..."):
            try:
                response = rag_chain.invoke(prompt)
                st.markdown(response)
                # Save assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.error(error_msg)