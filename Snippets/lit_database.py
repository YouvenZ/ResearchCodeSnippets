"""
Title: RAG Literature Database
Subtitle: Query your entire paper collection
Date: 2024-11-24
Category: AI Tools
Difficulty: Advanced
Tags: RAG, Database, Search, Literature
"""

from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

class LiteratureDatabase:
    def __init__(self, papers_dir: str):
        print("📚 Building literature database...")
        
        # Load all PDFs
        loader = DirectoryLoader(papers_dir, glob="**/*.pdf", 
                               loader_cls=PyPDFLoader)
        documents = loader.load()
        
        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        chunks = splitter.split_documents(documents)
        
        # Create vector store with persistence
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectorstore = Chroma.from_documents(
            chunks, embeddings, persist_directory="./literature_db"
        )
        
        # Setup QA chain
        llm = Ollama(model="llama2")
        self.qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5})
        )
        
        print(f"✓ Indexed {len(chunks)} chunks from {len(documents)} papers")
    
    def query(self, question: str):
        """Ask questions across all papers"""
        answer = self.qa.run(question)
        return answer
    
    def find_papers_about(self, topic: str, n: int = 5):
        """Find papers discussing specific topic"""
        docs = self.vectorstore.similarity_search(topic, k=n)
        
        results = []
        for doc in docs:
            results.append({
                'source': doc.metadata.get('source', 'Unknown'),
                'excerpt': doc.page_content[:300]
            })
        
        return results

# Usage
db = LiteratureDatabase('./papers')

# Query across all papers
answer = db.query("What are common evaluation metrics for NLP tasks?")
print(f"Answer: {answer}\n")

# Find relevant papers
papers = db.find_papers_about("attention mechanism", n=3)
for p in papers:
    print(f"📄 {p['source']}\n{p['excerpt']}...\n")