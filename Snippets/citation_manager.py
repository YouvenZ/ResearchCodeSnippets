"""
Title: BibTeX Citation Manager
Subtitle: Organize and format references automatically
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: BibTeX, Citations, References, Academic
"""

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

class CitationManager:
    def __init__(self, bib_file: str = 'references.bib'):
        self.bib_file = bib_file
        self.db = self._load_or_create()
    
    def _load_or_create(self):
        """Load existing or create new bibliography"""
        try:
            with open(self.bib_file) as f:
                return bibtexparser.load(f)
        except FileNotFoundError:
            return BibDatabase()
    
    def add_arxiv_paper(self, arxiv_id: str):
        """Add paper from ArXiv ID"""
        import arxiv
        
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(search.results())
        
        entry = {
            'ENTRYTYPE': 'article',
            'ID': arxiv_id.replace('.', '_'),
            'title': paper.title,
            'author': ' and '.join([a.name for a in paper.authors]),
            'year': str(paper.published.year),
            'journal': 'arXiv preprint',
            'eprint': arxiv_id,
            'archivePrefix': 'arXiv'
        }
        
        self.db.entries.append(entry)
        self._save()
    
    def _save(self):
        """Save bibliography to file"""
        writer = BibTexWriter()
        with open(self.bib_file, 'w') as f:
            f.write(writer.write(self.db))
    
    def search(self, keyword: str):
        """Search entries by keyword"""
        results = [e for e in self.db.entries 
                  if keyword.lower() in e.get('title', '').lower()]
        return results

# Usage
manager = CitationManager()
manager.add_arxiv_paper('2310.06825')  # Add a paper
matches = manager.search('transformer')