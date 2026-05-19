import streamlit as st
from core.pdf_processor import process_pdf
from core.embedder import embed_documents
from core.vector_store import index_chunks, delete_collection
from core.rag_chain import ask

st.set_page_config(page_title="Chat with your PDF", page_icon="📄")
st.title("📄 Chat with your PDF")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    if st.session_state.get("indexed_file") != uploaded_file.name:
        with st.spinner("Processing PDF..."):
            delete_collection()
            chunks     = process_pdf(uploaded_file)
            embeddings = embed_documents([c["text"] for c in chunks])
            index_chunks(chunks, embeddings)
            st.session_state.indexed_file = uploaded_file.name
            st.session_state.messages     = []
        st.success(f"Ready! {len(chunks)} chunks indexed.")

if st.session_state.get("indexed_file"):
    for msg in st.session_state.get("messages", []):
        st.chat_message(msg["role"]).write(msg["content"])

    if question := st.chat_input("Ask a question about your PDF..."):
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)

        with st.spinner("Thinking..."):
            answer = ask(question)

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)

else:
    st.info("Upload a PDF above to get started.")