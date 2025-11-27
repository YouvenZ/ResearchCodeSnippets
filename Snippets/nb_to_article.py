"""
Title: Notebook to Article Flow
Subtitle: One command: analysis → paper
Date: 2024-11-24
Category: Academic Writing
Difficulty: Intermediate
Tags: Jupyter, Workflow, Automation, Publishing
"""

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import subprocess

def notebook_to_article_pipeline(notebook_file: str):
    """Complete pipeline: execute → clean → convert → compile"""
    
    print("🔄 Starting pipeline...\n")
    
    # 1. Execute notebook
    print("1️⃣ Executing notebook...")
    with open(notebook_file) as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': './'}})
    
    executed = notebook_file.replace('.ipynb', '_executed.ipynb')
    with open(executed, 'w') as f:
        nbformat.write(nb, f)
    print(f"  ✓ Saved to {executed}")
    
    # 2. Convert to LaTeX
    print("\n2️⃣ Converting to LaTeX...")
    tex_file = executed.replace('.ipynb', '.tex')
    subprocess.run(['jupyter', 'nbconvert', '--to', 'latex', 
                   executed, '--output', tex_file], check=True)
    print(f"  ✓ Created {tex_file}")
    
    # 3. Clean LaTeX (remove Jupyter artifacts)
    print("\n3️⃣ Cleaning LaTeX...")
    with open(tex_file) as f:
        content = f.read()
    
    # Remove notebook-specific commands
    clean = content.replace('\\maketitle', '')
    clean = clean.replace('\\tableofcontents', '')
    
    # Wrap in article template
    article = f"""\\documentclass{{article}}
\\usepackage{{graphicx,amsmath,booktabs}}
\\title{{Generated from Analysis}}
\\author{{Your Name}}

\\begin{{document}}
\\maketitle

{clean}

\\end{{document}}
"""
    
    clean_file = 'article.tex'
    with open(clean_file, 'w') as f:
        f.write(article)
    print(f"  ✓ Created clean {clean_file}")
    
    # 4. Compile to PDF
    print("\n4️⃣ Compiling to PDF...")
    subprocess.run(['pdflatex', clean_file], 
                  capture_output=True, check=True)
    print("  ✓ Created article.pdf")
    
    print("\n✅ Pipeline complete!")
    print("📄 article.pdf ready for submission")

# Usage - write analysis in notebook with markdown headers
notebook_to_article_pipeline('analysis.ipynb')