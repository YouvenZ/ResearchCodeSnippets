"""
Title: Quick ArXiv Search
Subtitle: Find papers in 3 lines of code
Date: 2024-11-24
Category: Research
Difficulty: Beginner
Tags: ArXiv, Search, Quick, Papers
"""

import arxiv

# Search papers by keyword
search = arxiv.Search(query="large language models", max_results=5)

# Get results with key info
for paper in search.results():
    print(f"📄 {paper.title}")
    print(f"👥 {', '.join(a.name for a in paper.authors[:3])}")
    print(f"📅 {paper.published.date()}")
    print(f"🔗 {paper.pdf_url}\n")