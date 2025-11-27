"""
Title: Smart Citation Suggester
Subtitle: LLM-powered citation recommendations
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: LLM, Citations, Writing, RAG
"""

from langchain.llms import Ollama
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import bibtexparser

def build_citation_database(bib_file: str):
    """Build searchable citation database"""
    
    # Parse BibTeX
    with open(bib_file) as f:
        bib_db = bibtexparser.load(f)
    
    # Create documents from entries
    docs = []
    for entry in bib_db.entries:
        text = f"{entry.get('title', '')} {entry.get('abstract', '')}"
        docs.append({
            'text': text,
            'metadata': entry
        })
    
    # Create vector store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    texts = [d['text'] for d in docs]
    metadatas = [d['metadata'] for d in docs]
    
    vectorstore = Chroma.from_texts(texts, embeddings, metadatas=metadatas)
    
    print(f"✓ Indexed {len(docs)} papers")
    return vectorstore

def suggest_citations(text: str, vectorstore, n: int = 5):
    """Suggest relevant citations for a text passage"""
    
    # Find similar papers
    results = vectorstore.similarity_search(text, k=n)
    
    suggestions = []
    for doc in results:
        meta = doc.metadata
        citation = f"{meta.get('author', 'Unknown')} ({meta.get('year', 'N/A')})"
        suggestions.append({
            'citation': citation,
            'title': meta.get('title', 'N/A'),
            'key': meta.get('ID', 'N/A')
        })
    
    return suggestions

# Usage
vectorstore = build_citation_database('references.bib')

text = "Transformers have revolutionized natural language processing"
suggestions = suggest_citations(text, vectorstore, n=3)

print("💡 Suggested citations:")
for s in suggestions:
    print(f"  [{s['key']}] {s['citation']}: {s['title'][:60]}...")