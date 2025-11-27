"""
Title: DOI to BibTeX
Subtitle: Generate citations from DOI instantly
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: DOI, BibTeX, Citations, Automation
"""

import requests

def doi_to_bibtex(doi: str) -> str:
    """Convert DOI to BibTeX entry using CrossRef"""
    
    url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    
    response = requests.get(url)
    
    if response.ok:
        return response.text
    else:
        return f"Error: Could not fetch BibTeX for {doi}"

def batch_doi_to_bib(dois: list, output_file: str = 'references.bib'):
    """Convert multiple DOIs to BibTeX file"""
    
    entries = []
    for doi in dois:
        bib = doi_to_bibtex(doi)
        if not bib.startswith("Error"):
            entries.append(bib)
            print(f"✓ {doi}")
        else:
            print(f"✗ {doi}")
    
    with open(output_file, 'w') as f:
        f.write('\n\n'.join(entries))
    
    print(f"\n✓ Saved {len(entries)} entries to {output_file}")

# Usage
dois = ['10.1038/nature14539', '10.1126/science.aaa8415']
batch_doi_to_bib(dois)