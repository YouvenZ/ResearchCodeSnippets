"""
Title: Auto Literature Matrix Builder
Subtitle: Generate comparison tables from papers
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: RAG, Analysis, Table, Comparison
"""

from langchain.llms import Ollama
from langchain.document_loaders import PyPDFLoader
import pandas as pd

def create_literature_matrix(paper_files: list, aspects: list):
    """Create comparison matrix from multiple papers"""
    
    llm = Ollama(model="llama2", temperature=0.2)
    
    matrix_data = []
    
    for pdf_file in paper_files:
        # Extract paper content
        loader = PyPDFLoader(pdf_file)
        pages = loader.load()
        content = " ".join([p.page_content for p in pages[:3]])[:3000]
        
        # Extract key aspects
        prompt = f"""Extract from this paper:

{content}

For each aspect, provide brief answer:
{chr(10).join([f"- {aspect}" for aspect in aspects])}

Format: Aspect: Answer (one line each)

Extraction:"""
        
        response = llm(prompt)
        
        # Parse response
        row = {'Paper': pdf_file.split('/')[-1]}
        for line in response.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                row[key.strip()] = value.strip()
        
        matrix_data.append(row)
        print(f"✓ Processed {pdf_file}")
    
    # Create DataFrame and save
    df = pd.DataFrame(matrix_data)
    df.to_csv('literature_matrix.csv', index=False)
    
    # Create markdown table
    md_table = df.to_markdown(index=False)
    with open('literature_matrix.md', 'w') as f:
        f.write("# Literature Comparison Matrix\n\n")
        f.write(md_table)
    
    print(f"\n✅ Matrix created with {len(matrix_data)} papers")
    return df

# Usage
papers = ['paper1.pdf', 'paper2.pdf', 'paper3.pdf']
aspects = ['Method', 'Dataset', 'Main Result', 'Limitation']
matrix = create_literature_matrix(papers, aspects)