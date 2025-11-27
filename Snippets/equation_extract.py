"""
Title: Equation Extractor
Subtitle: Pull all equations from LaTeX/Markdown
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: Equations, LaTeX, Extraction, Math
"""

import re

def extract_equations(file_path: str):
    """Extract and catalog all equations from document"""
    
    with open(file_path) as f:
        content = f.read()
    
    # Find inline math ($...$)
    inline = re.findall(r'\$([^\$]+)\$', content)
    
    # Find display math ($$...$$, \[...\], equation environment)
    display = []
    display += re.findall(r'\$\$(.+?)\$\$', content, re.DOTALL)
    display += re.findall(r'\\\[(.+?)\\\]', content, re.DOTALL)
    display += re.findall(
        r'\\begin\{equation\*?\}(.+?)\\end\{equation\*?\}', 
        content, re.DOTALL
    )
    
    # Create equation catalog
    catalog = f"""# Equation Catalog for {file_path}

## Inline Equations ({len(inline)})
"""
    
    for i, eq in enumerate(inline, 1):
        catalog += f"{i}. `${eq}$`\n"
    
    catalog += f"\n## Display Equations ({len(display)})\n\n"
    
    for i, eq in enumerate(display, 1):
        catalog += f"### Equation {i}\n```latex\n{eq.strip()}\n```\n\n"
    
    # Save catalog
    catalog_file = file_path.replace('.tex', '_equations.md').replace('.md', '_equations.md')
    with open(catalog_file, 'w') as f:
        f.write(catalog)
    
    print(f"✓ Found {len(inline)} inline equations")
    print(f"✓ Found {len(display)} display equations")
    print(f"✓ Saved catalog to {catalog_file}")
    
    return {'inline': inline, 'display': display}

# Usage - review all equations before submission
equations = extract_equations('paper.tex')
print(f"\nMost complex: {max(equations['display'], key=len)[:50]}...")