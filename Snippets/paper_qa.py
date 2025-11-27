"""
Title: Paper Q&A with Local LLM
Subtitle: Ask questions about research papers
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: LLM, RAG, QA, Research
"""

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama

def setup_paper_qa(pdf_path: str):
    """Setup RAG system for paper Q&A"""
    
    # Load and split PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)
    
    # Create vector store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # Setup LLM (using local Ollama)
    llm = Ollama(model="llama2")
    
    print(f"✓ Indexed {len(chunks)} chunks from paper")
    
    return vectorstore, llm

def ask_paper(question: str, vectorstore, llm):
    """Ask question about the paper"""
    
    # Retrieve relevant chunks
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Generate answer
    prompt = f"Context from paper:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    answer = llm(prompt)
    
    return answer

# Usage
vectorstore, llm = setup_paper_qa("research_paper.pdf")
answer = ask_paper("What is the main contribution?", vectorstore, llm)
print(answer)