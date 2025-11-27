"""
Title: Notebook Slides Exporter
Subtitle: Present directly from Jupyter
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: Jupyter, Slides, RISE, Presentation
"""

import nbformat
from nbformat.v4 import new_markdown_cell

def notebook_to_slides(notebook_file: str):
    """Convert Jupyter notebook to reveal.js slides"""
    
    # Load notebook
    with open(notebook_file) as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add slide metadata to cells
    slide_types = ['slide', 'subslide', 'fragment', 'skip', 'notes']
    
    # Configure first cell as title
    if nb.cells:
        nb.cells[0].metadata['slideshow'] = {'slide_type': 'slide'}
    
    # Auto-detect slides from markdown headers
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown':
            if cell.source.startswith('# '):
                cell.metadata['slideshow'] = {'slide_type': 'slide'}
            elif cell.source.startswith('## '):
                cell.metadata['slideshow'] = {'slide_type': 'subslide'}
        
        # Code cells as fragments
        elif cell.cell_type == 'code':
            if 'slideshow' not in cell.metadata:
                cell.metadata['slideshow'] = {'slide_type': 'fragment'}
    
    # Add presentation metadata
    nb.metadata['celltoolbar'] = 'Slideshow'
    nb.metadata['rise'] = {
        'theme': 'serif',
        'transition': 'slide',
        'scroll': True
    }
    
    # Save slides version
    output_file = notebook_file.replace('.ipynb', '_slides.ipynb')
    with open(output_file, 'w') as f:
        nbformat.write(nb, f)
    
    print(f"✓ Created {output_file}")
    print("📊 Present with:")
    print(f"   jupyter nbconvert {output_file} --to slides --post serve")
    print("   OR install RISE: pip install RISE")

# Usage - turn analysis notebook into presentation
notebook_to_slides('analysis.ipynb')