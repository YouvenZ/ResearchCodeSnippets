"""
Title: Bulk Paper Downloader
Subtitle: Download multiple papers by ID
Date: 2024-11-24
Category: Research
Difficulty: Beginner
Tags: ArXiv, Download, Bulk, Automation
"""

import arxiv
from pathlib import Path

def download_papers(arxiv_ids: list, output_dir: str = 'papers'):
    """Download multiple ArXiv papers by ID"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    for paper_id in arxiv_ids:
        try:
            # Get paper info
            search = arxiv.Search(id_list=[paper_id])
            paper = next(search.results())
            
            # Create filename from title
            safe_title = "".join(c for c in paper.title 
                               if c.isalnum() or c in (' ', '-'))[:50]
            filename = f"{output_dir}/{paper_id}_{safe_title}.pdf"
            
            # Download
            paper.download_pdf(filename=filename)
            print(f"✓ {paper.title[:60]}")
            
        except Exception as e:
            print(f"✗ Failed: {paper_id} ({e})")

# Usage - download multiple papers
papers = ['2310.06825', '2303.08774', '2307.09288']
download_papers(papers)