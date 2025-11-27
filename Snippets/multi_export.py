"""
Title: Multi-Format Export
Subtitle: Export paper to PDF, HTML, DOCX at once
Date: 2024-11-24
Category: Academic Writing
Difficulty: Intermediate
Tags: Export, Pandoc, MultiFormat, Publishing
"""

import subprocess
from pathlib import Path

def export_paper_all_formats(source_file: str):
    """Export paper to multiple formats for different venues"""
    
    formats = {
        'pdf': {
            'cmd': ['pandoc', source_file, '-o', 'paper.pdf',
                   '--pdf-engine=xelatex', '--number-sections'],
            'desc': 'PDF for printing/submission'
        },
        'html': {
            'cmd': ['pandoc', source_file, '-o', 'paper.html',
                   '--standalone', '--mathjax', '--toc',
                   '--css=academic.css'],
            'desc': 'HTML for website'
        },
        'docx': {
            'cmd': ['pandoc', source_file, '-o', 'paper.docx',
                   '--reference-doc=template.docx'],
            'desc': 'DOCX for collaborators'
        },
        'epub': {
            'cmd': ['pandoc', source_file, '-o', 'paper.epub',
                   '--toc'],
            'desc': 'EPUB for reading'
        }
    }
    
    results = {}
    
    print("📦 Exporting to multiple formats...\n")
    
    for fmt, config in formats.items():
        try:
            subprocess.run(config['cmd'], check=True, 
                         capture_output=True)
            results[fmt] = 'success'
            print(f"✓ {fmt.upper()}: {config['desc']}")
        except subprocess.CalledProcessError as e:
            results[fmt] = 'failed'
            print(f"✗ {fmt.upper()}: Failed")
    
    # Create distribution folder
    dist = Path('distribution')
    dist.mkdir(exist_ok=True)
    
    for fmt in results:
        if results[fmt] == 'success':
            source = f"paper.{fmt}"
            if Path(source).exists():
                Path(source).rename(dist / source)
    
    print(f"\n✅ Exported {sum(1 for v in results.values() if v == 'success')} formats")
    print(f"📁 Files in ./distribution/")

# Usage - one command to export everything
export_paper_all_formats('paper.md')  # or paper.tex