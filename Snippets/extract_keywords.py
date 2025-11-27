"""
Title: Paper Keywords Extractor
Subtitle: Auto-extract key terms from abstracts
Date: 2024-11-24
Category: NLP
Difficulty: Beginner
Tags: NLP, Keywords, TextAnalysis, Research
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keywords(text: str, top_n: int = 10):
    """Extract key terms using TF-IDF"""
    
    # Initialize vectorizer
    vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
    
    # Fit and transform
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    
    # Get top keywords
    scores = tfidf_matrix.toarray()[0]
    top_indices = scores.argsort()[-top_n:][::-1]
    
    keywords = [(feature_names[i], scores[i]) for i in top_indices]
    
    return keywords

# Usage
abstract = "Transformers have revolutionized natural language processing..."
keywords = extract_keywords(abstract, top_n=5)

for word, score in keywords:
    print(f"🔑 {word}: {score:.3f}")