# modules/rag.py

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from .config import OLLAMA_MODEL

def create_rag_chain(db):
    llm = Ollama(model=OLLAMA_MODEL)

    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context. 
    Think step-by-step before providing a detailed answer.

    <Context>
    {context}
    </Context>

    Question: {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = db.as_retriever()

    return create_retrieval_chain(retriever, document_chain)
