"""
Title: Abstract Summarizer
Subtitle: Extract key sentences from abstract
Date: 2024-11-24
Category: NLP
Difficulty: Beginner
Tags: Abstract, Summarization, NLP, Writing
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def summarize_abstract(abstract: str, n_sentences: int = 3) -> dict:
    """Extract most important sentences from abstract"""
    
    # Split into sentences
    sentences = [s.strip() for s in abstract.split('.') if s.strip()]
    
    if len(sentences) <= n_sentences:
        return {
            'summary': abstract,
            'key_sentences': sentences,
            'compression': 1.0
        }
    
    # Calculate TF-IDF for each sentence
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Score sentences by their mean TF-IDF
    scores = tfidf_matrix.mean(axis=1).A1
    
    # Get top sentences
    top_indices = scores.argsort()[-n_sentences:][::-1]
    top_indices = sorted(top_indices)  # Maintain order
    
    key_sentences = [sentences[i] for i in top_indices]
    summary = '. '.join(key_sentences) + '.'
    
    return {
        'summary': summary,
        'key_sentences': key_sentences,
        'compression': len(summary) / len(abstract),
        'original_length': len(abstract),
        'summary_length': len(summary)
    }

# Usage
abstract = """Deep learning has revolutionized natural language processing. 
Transformer models have shown remarkable performance across various tasks. 
However, these models require significant computational resources. 
Our work addresses this limitation by proposing an efficient architecture. 
We achieve 95% of the performance with 50% fewer parameters."""

result = summarize_abstract(abstract, n_sentences=2)
print(f"Original: {result['original_length']} chars")
print(f"Summary: {result['summary_length']} chars")
print(f"\n{result['summary']}")