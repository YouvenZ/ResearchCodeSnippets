"""
Title: Batch ArXiv Downloader
Subtitle: Download papers efficiently with metadata
Date: 2024-11-24
Category: Research Tools
Difficulty: Intermediate
Tags: ArXiv, PDF, Automation, Research
"""

import arxiv
import requests
from pathlib import Path
from typing import List

def download_arxiv_papers(queries: List[str], 
                         max_per_query: int = 5,
                         output_dir: str = 'papers'):
    """Download papers from ArXiv with metadata"""
    
    Path(output_dir).mkdir(exist_ok=True)
    downloaded = []
    
    for query in queries:
        search = arxiv.Search(
            query=query,
            max_results=max_per_query,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        for paper in search.results():
            # Create safe filename
            safe_title = "".join(c for c in paper.title 
                               if c.isalnum() or c in (' ', '-', '_'))
            filename = f"{safe_title[:50]}.pdf"
            filepath = Path(output_dir) / filename
            
            # Download PDF
            paper.download_pdf(filename=str(filepath))
            
            # Save metadata
            metadata = {
                'title': paper.title,
                'authors': [a.name for a in paper.authors],
                'abstract': paper.summary,
                'url': paper.pdf_url,
                'published': str(paper.published)
            }
            
            downloaded.append(metadata)
            print(f"✓ Downloaded: {paper.title[:60]}...")
    
    return downloaded

# Usage
papers = download_arxiv_papers(
    ['deep learning', 'transformers'],
    max_per_query=3
)