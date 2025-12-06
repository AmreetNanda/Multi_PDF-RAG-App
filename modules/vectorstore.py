import os
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from .config import VECTOR_DB_DIR, OLLAMA_MODEL

emb = OllamaEmbeddings(model=OLLAMA_MODEL)

def get_multi_db_path(pdf_names):
    """Create a consistent directory name for multiple PDFs."""
    safe_name = "_".join([name.replace(" ", "_").replace(".pdf", "") for name in pdf_names])
    return os.path.join(VECTOR_DB_DIR, f"{safe_name}_multi_chroma")

def build_or_load_chroma_multi(pdf_names, documents=None):
    """Load or build a Chroma DB for multiple PDFs."""
    db_path = get_multi_db_path(pdf_names)

    if os.path.exists(db_path):
        return Chroma(
            persist_directory=db_path,
            embedding_function=emb
        )

    if documents is None:
        raise ValueError("Documents required to build new vector DB.")

    os.makedirs(db_path, exist_ok=True)
    db = Chroma.from_documents(
        documents,
        emb,
        persist_directory=db_path
    )
    db.persist()

    return db
