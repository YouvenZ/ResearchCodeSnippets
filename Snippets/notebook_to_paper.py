"""
Title: Jupyter to Paper
Subtitle: Transform notebooks into publications
Date: 2024-11-24
Category: Academic Writing
Difficulty: Intermediate
Tags: Jupyter, Notebook, LaTeX, Conversion
"""

import nbformat
from nbconvert import LatexExporter

def notebook_to_paper(notebook_file: str):
    """Convert Jupyter notebook to LaTeX paper"""
    
    # Load notebook
    with open(notebook_file) as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add paper metadata to first cell
    paper_template = """% Generated from Jupyter Notebook
\\documentclass{article}
\\usepackage{graphicx,amsmath,booktabs}

\\title{Paper Title from Notebook}
\\author{Your Name}

\\begin{document}
\\maketitle

"""
    
    # Configure exporter
    exporter = LatexExporter()
    exporter.template_name = 'article'
    
    # Convert
    (body, resources) = exporter.from_notebook_node(nb)
    
    # Clean up output (remove notebook-specific formatting)
    body = body.replace('\\section{', '\\section*{')
    
    # Save
    output_file = notebook_file.replace('.ipynb', '.tex')
    with open(output_file, 'w') as f:
        f.write(body)
    
    # Also save as PDF-ready version
    pdf_ready = f"{paper_template}\n{body}\n\\end{{document}}"
    with open('paper_from_notebook.tex', 'w') as f:
        f.write(pdf_ready)
    
    print(f"✓ Converted {notebook_file}")
    print("✓ Created paper_from_notebook.tex")
    print("📊 Figures automatically included!")

# Usage - structure your notebook with markdown headers
# # Introduction
# Your intro text
# ## Methods  
# ```python
# your code
#