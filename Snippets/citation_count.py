"""
Title: Citation Count Checker
Subtitle: Get citation metrics instantly
Date: 2024-11-24
Category: Research
Difficulty: Beginner
Tags: Citations, Metrics, SemanticScholar, Impact
"""

import requests

def get_citation_count(paper_title: str):
    """Get citation count from Semantic Scholar"""
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    response = requests.get(url, params={
        'query': paper_title,
        'fields': 'title,citationCount,year,authors'
    })
    
    if response.ok and response.json()['data']:
        paper = response.json()['data'][0]
        return {
            'title': paper['title'],
            'citations': paper['citationCount'],
            'year': paper['year'],
            'cites_per_year': paper['citationCount'] / (2024 - paper['year'] + 1)
        }

# Usage
metrics = get_citation_count("Attention is All You Need")
print(f"📊 {metrics['citations']} citations")
print(f"📈 {metrics['cites_per_year']:.1f} citations/year")