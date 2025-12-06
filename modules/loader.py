# # modules/loader.py

# from langchain_community.document_loaders import PyPDFLoader
# from .config import PDF_PATH

# def load_pdf():
#     loader = PyPDFLoader(PDF_PATH)
#     return loader.load()

# modules/loader.py

import os
from langchain_community.document_loaders import PyPDFLoader
from .config import PDF_UPLOAD_DIR

def save_uploaded_pdf(uploaded_file):
    """Save the uploaded file to PDF_UPLOAD_DIR."""
    os.makedirs(PDF_UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(PDF_UPLOAD_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def load_pdf(path):
    """Load a PDF from a given path."""
    loader = PyPDFLoader(path)
    return loader.load()
