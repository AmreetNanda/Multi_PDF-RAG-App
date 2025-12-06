# # # modules/vectorstore.py

# # import os
# # from langchain_community.embeddings import OllamaEmbeddings
# # from langchain_community.vectorstores import Chroma
# # from .config import CHROMA_DB_DIR, OLLAMA_MODEL

# # emb = OllamaEmbeddings(model=OLLAMA_MODEL)

# # def build_or_load_chroma(documents=None):
# #     """
# #     If DB exists → load it
# #     Else → create and persist
# #     """
# #     if os.path.exists(CHROMA_DB_DIR):
# #         return Chroma(
# #             persist_directory=CHROMA_DB_DIR,
# #             embedding_function=emb
# #         )

# #     if documents is None:
# #         raise ValueError("No documents provided to build new Chroma DB.")

# #     db = Chroma.from_documents(
# #         documents,
# #         emb,
# #         persist_directory=CHROMA_DB_DIR
# #     )
# #     db.persist()
# #     return db


# # modules/vectorstore.py

# import os
# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma
# from .config import VECTOR_DB_DIR, OLLAMA_MODEL

# emb = OllamaEmbeddings(model=OLLAMA_MODEL)

# def get_db_path(pdf_name):
#     """Return vector DB directory path for a given PDF."""
#     safe_name = pdf_name.replace(" ", "_").replace(".pdf", "")
#     return os.path.join(VECTOR_DB_DIR, f"{safe_name}_chroma")

# def build_or_load_chroma(pdf_name, documents=None):
#     """Load or create a Chroma DB for a specific PDF."""
#     db_path = get_db_path(pdf_name)

#     # Load existing DB
#     if os.path.exists(db_path):
#         return Chroma(
#             persist_directory=db_path,
#             embedding_function=emb
#         )

#     # Build new DB
#     if documents is None:
#         raise ValueError("Documents required to create new vector DB.")

#     os.makedirs(db_path, exist_ok=True)
#     db = Chroma.from_documents(
#         documents,
#         emb,
#         persist_directory=db_path
#     )
#     db.persist()

#     return db


# modules/vectorstore.py

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
