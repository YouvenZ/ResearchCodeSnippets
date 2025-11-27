"""
Title: Abstract to Keywords
Subtitle: Extract keywords from abstract
Date: 2024-11-24
Category: AI Tools
Difficulty: Beginner
Tags: LLM, Keywords, NLP, Extraction
"""

from langchain.llms import Ollama

def extract_keywords(abstract: str, n: int = 5):
    """Extract keywords from abstract using LLM"""
    
    llm = Ollama(model="llama2", temperature=0.3)
    
    prompt = f"""Extract {n} most important keywords from this abstract:

{abstract}

Keywords should be:
- Single words or short phrases (2-3 words max)
- Specific to the research
- Commonly used in the field
- Suitable for indexing

List {n} keywords, comma-separated:"""
    
    keywords = llm(prompt)
    keyword_list = [k.strip() for k in keywords.split(',')]
    
    return keyword_list[:n]

def suggest_mesh_terms(abstract: str):
    """Suggest MeSH terms for biomedical papers"""
    
    llm = Ollama(model="llama2", temperature=0.2)
    
    prompt = f"""Suggest Medical Subject Headings (MeSH) terms for this abstract:

{abstract}

Provide 5-7 MeSH terms that best describe this research.
Use standard MeSH vocabulary.

MeSH terms:"""
    
    mesh_terms = llm(prompt)
    
    return mesh_terms.strip()

# Usage
abstract = """We propose a novel deep learning architecture for natural language 
understanding. Our model combines transformers with graph neural networks to 
capture both sequential and structural information. Experiments show 15% 
improvement over baseline methods on benchmark datasets."""

keywords = extract_keywords(abstract, n=5)
print("Keywords:", keywords)

# For biomedical papers
bio_abstract = """We developed a new method for protein structure prediction 
using deep learning. Results show high accuracy on benchmark datasets."""

mesh = suggest_mesh_terms(bio_abstract)
print("\nMeSH terms:", mesh)