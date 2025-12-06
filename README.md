# 📚 Multi PDF RAG System (Llama3 + Chroma)
---
This project creates a Retrieval-Augmented Generation (RAG) pipeline using:

- **Llama3**
- **ChromaDB (local vector store)**
- **LangChain**
- **Streamlit UI**
- **PDF document ingestion**

## Requirements
- Python 3.12+
- Local Ollama server with Llama3 model
- GPU-enabled environment recommended for faster response

## Features
✔ Load and parse multiple PDF documents  
✔ Split text into overlapping chunks  
✔ Embed chunks using Ollama Llama3  
✔ Store embeddings locally with Chroma  
✔ Query the document using a RAG pipeline  
✔ Streamlit interface for user queries  

## Technologies Used:
- Streamlit, Python, ChromaDB, Ollama
- Models used: Llama3

## Project Structure

```bash
Langchain_basic/
├── db/                  # For storing and loading the vector database
├── uploaded_pdfs/       # Uploaded PDFs will be stored here
├── app.py               # Streamlit app for user
├── modules/
│ ├── loader.py
│ ├── splitter.py
│ ├── vectorstore.py
│ ├── rag.py
│ └── config.py
├── README.md
├── rag.ipynb            # simple rag implementation with jupyter notebook
└─ requirements.txt      # Python dependencies
```

## 🧠 How It Works 
- **Load PDF** → Convert into pages/text  
-  **Split text** → Using `RecursiveCharacterTextSplitter`  
-  **Embed chunks** → Using Llama3 from Ollama  
-  **Store embeddings** → Locally in `./db/chroma_db`  
-  **RAG Query** → Retrieve + Generate answer  

## 📝 Customization
You can modify as per your requirement:
- `config.py` for chunk sizes, paths, model name  
- PDF file path  
- Prompt template in `docrag.py`  
- Streamlit UI 

## Installation

## 🛠 Installation

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/Multi_PDF-RAG-App.git
cd multipdfrag
```
### 2. Requirements.txt
```bash
langchain
langchain_community
langchain-core
langchain-classic
ipykernel
streamlit
python-dotenv
langchain_objectbox
sse_starlette
bs4
pypdf
chromadb
faiss-cpu
beautifulsoup4
pypdf2
torch
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Streamlit app
```bash
streamlit run app.py

```
Open in your browser:
```
👉 http://localhost:8501/
👉 Drag and drop one or multiple PDF files 
👉 Wait till it generates the db and stores it 
👉 After that it will show the text box for user queries
👉 Enter your query and hit Enter
👉 It will generate the context based on the uploaded pdfs
```

## Demo
https://github.com/user-attachments/assets/f2f3cd27-78a5-431e-b4b6-b8f7a05ef3af

## License
[MIT](https://choosealicense.com/licenses/mit/)
