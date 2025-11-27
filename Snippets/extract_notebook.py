"""
Title: Notebook Section Extractor
Subtitle: Pull specific parts from notebooks
Date: 2024-11-24
Category: Academic Writing
Difficulty: Intermediate
Tags: Jupyter, Extraction, Markdown, Sections
"""

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

def extract_notebook_sections(notebook_file: str, sections: list):
    """Extract specific sections from notebook for paper"""
    
    # Load notebook
    with open(notebook_file) as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create new notebook for paper
    paper_nb = new_notebook()
    
    current_section = None
    include_next = False
    
    for cell in nb.cells:
        # Check if this is a section header
        if cell.cell_type == 'markdown' and cell.source.startswith('#'):
            section_name = cell.source.split('\n')[0].strip('# ')
            current_section = section_name
            include_next = any(s in section_name for s in sections)
        
        # Include cells from desired sections
        if include_next:
            paper_nb.cells.append(cell)
    
    # Save extracted notebook
    output_file = notebook_file.replace('.ipynb', '_paper.ipynb')
    with open(output_file, 'w') as f:
        nbformat.write(paper_nb, f)
    
    print(f"✓ Extracted {len(paper_nb.cells)} cells")
    print(f"✓ Saved to {output_file}")
    
    # Also export as markdown
    markdown = ""
    for cell in paper_nb.cells:
        if cell.cell_type == 'markdown':
            markdown += cell.source + "\n\n"
        elif cell.cell_type == 'code':
            markdown += f"```python\n{cell.source}\n```\n\n"
    
    md_file = output_file.replace('.ipynb', '.md')
    with open(md_file, 'w') as f:
        f.write(markdown)
    
    print(f"✓ Also saved as {md_file}")

# Usage - extract only Methods and Results sections
extract_notebook_sections(
    'full_analysis.ipynb',
    sections=['Methods', 'Results', 'Discussion']
)