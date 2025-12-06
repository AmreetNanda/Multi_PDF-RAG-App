# app.py

import streamlit as st
from modules.loader import save_uploaded_pdf, load_pdf
from modules.splitter import split_documents
from modules.vectorstore import build_or_load_chroma_multi
from modules.docrag import create_rag_chain

st.set_page_config(page_title="Multi-PDF RAG with Llama3", layout="wide")
st.title("📘 Multi-PDF RAG Assistant (Upload PDFs → Ask Questions)")

st.write("Upload one or more PDFs, wait for processing, and then ask any question about them.")

# -------------------------------------------------------------------
# 📌 MULTIPLE PDF UPLOAD
# -------------------------------------------------------------------
uploaded_files = st.file_uploader(
    "📄 Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    all_docs = []
    pdf_names = []

    for uploaded_file in uploaded_files:
        file_path = save_uploaded_pdf(uploaded_file)
        pdf_names.append(uploaded_file.name)

        with st.spinner(f"Loading {uploaded_file.name}..."):
            docs = load_pdf(file_path)

        with st.spinner(f"Splitting {uploaded_file.name} into chunks..."):
            chunks = split_documents(docs)
            all_docs.extend(chunks)

    # Build or load a DB for all uploaded PDFs
    with st.spinner("Building vector database for all PDFs..."):
        db = build_or_load_chroma_multi(pdf_names, all_docs)

    st.session_state["db_ready"] = True
    st.session_state["pdf_names"] = pdf_names
    st.success("Vector DB is ready! You can now ask questions below.")

# -------------------------------------------------------------------
# 📌 QUESTION BOX
# -------------------------------------------------------------------
st.subheader("❓ Ask a question related to ANY of the uploaded PDFs:")

if "db_ready" in st.session_state and st.session_state["db_ready"]:
    query = st.text_input("Enter your question here:")

    if query:
        pdf_names = st.session_state["pdf_names"]
        db = build_or_load_chroma_multi(pdf_names)

        rag_chain = create_rag_chain(db)

        with st.spinner("Generating answer..."):
            response = rag_chain.invoke({"input": query})

        st.subheader("📘 Answer:")
        st.write(response["answer"])

        st.subheader("📚 Retrieved Context Chunks:")
        for doc in response["context"]:
            with st.expander("View Chunk"):
                st.write(doc.page_content)
else:
    st.info("Upload PDFs to begin.")
