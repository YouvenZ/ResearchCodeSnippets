"""
Title: PDF Text Extractor
Subtitle: Extract text from papers quickly
Date: 2024-11-24
Category: Data Processing
Difficulty: Beginner
Tags: PDF, Text, Extraction, Processing
"""

import PyPDF2

def extract_pdf_text(pdf_path: str, pages: list = None) -> str:
    """Extract text from PDF pages"""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Extract specific pages or all
        pages = pages or range(len(reader.pages))
        
        text = ""
        for page_num in pages:
            text += reader.pages[page_num].extract_text()
        
        return text

# Usage - extract abstract (usually page 1)
abstract = extract_pdf_text("paper.pdf", pages=[0])
print(abstract[:500])  # First 500 chars

# Full paper
full_text = extract_pdf_text("paper.pdf")
print(f"📄 Extracted {len(full_text)} characters")