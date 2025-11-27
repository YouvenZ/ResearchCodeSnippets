"""
Title: Bibliography Formatter
Subtitle: Format .bib file for different journals
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: BibTeX, Bibliography, Formatting, Journals
"""

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def format_bibliography(bib_file: str, style: str = 'ieee'):
    """Format bibliography according to journal style"""
    
    # Load bibliography
    with open(bib_file) as f:
        bib_db = bibtexparser.load(f)
    
    # Style-specific formatting
    for entry in bib_db.entries:
        
        if style == 'ieee':
            # IEEE style: abbreviated names, no DOI
            if 'doi' in entry:
                del entry['doi']
            if 'url' in entry:
                del entry['url']
                
        elif style == 'apa':
            # APA style: full names, include DOI
            if 'doi' not in entry and 'url' in entry:
                entry['doi'] = entry['url'].split('doi.org/')[-1]
        
        elif style == 'nature':
            # Nature style: minimal fields
            keep_fields = ['author', 'title', 'journal', 'year', 'volume', 'pages']
            entry_keys = list(entry.keys())
            for key in entry_keys:
                if key not in keep_fields and key != 'ID' and key != 'ENTRYTYPE':
                    del entry[key]
        
        # Clean up author field
        if 'author' in entry:
            entry['author'] = entry['author'].replace('\n', ' ')
    
    # Save formatted bibliography
    writer = BibTexWriter()
    writer.indent = '  '
    writer.order_entries_by = ('year', 'author')
    
    output_file = bib_file.replace('.bib', f'_{style}.bib')
    with open(output_file, 'w') as f:
        f.write(writer.write(bib_db))
    
    print(f"✓ Formatted {len(bib_db.entries)} entries")
    print(f"✓ Saved to {output_file}")
    print(f"📚 Style: {style.upper()}")

# Usage
format_bibliography('references.bib', style='ieee')
format_bibliography('references.bib', style='nature')