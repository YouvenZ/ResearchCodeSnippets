"""
Title: Paper Gap Finder
Subtitle: AI identifies research gaps in literature
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: LLM, Analysis, Gaps, Literature
"""

from langchain.llms import Ollama
from langchain.document_loaders import PyPDFLoader

def find_research_gaps(paper_files: list):
    """Analyze papers to identify research gaps"""
    
    llm = Ollama(model="llama2", temperature=0.3)
    
    # Extract key info from papers
    papers_content = []
    for pdf_file in paper_files:
        loader = PyPDFLoader(pdf_file)
        pages = loader.load()
        
        # Get abstract and conclusion (usually first and last pages)
        abstract = pages[0].page_content[:1000]
        conclusion = pages[-1].page_content[:1000] if len(pages) > 1 else ""
        
        papers_content.append({
            'file': pdf_file,
            'content': f"{abstract}\n\n{conclusion}"
        })
    
    # Analyze for gaps
    combined = "\n\n---\n\n".join([p['content'] for p in papers_content])
    
    prompt = f"""Analyze these research papers and identify gaps:

{combined[:4000]}

Identify:
1. What has been done (summary)
2. What is missing (gaps)
3. Contradictions or disagreements
4. Unexplored directions
5. Potential research opportunities

Analysis:"""
    
    analysis = llm(prompt)
    
    # Create report
    report = f"""# Research Gap Analysis

## Papers Analyzed
{chr(10).join([f"- {p['file']}" for p in papers_content])}

## Findings

{analysis}

## Recommendations

Based on the gaps identified, consider research in:
1. [Gap 1 from analysis]
2. [Gap 2 from analysis]
3. [Gap 3 from analysis]
"""
    
    with open('gap_analysis.md', 'w') as f:
        f.write(report)
    
    print("✓ Gap analysis complete")
    print("📊 Saved to gap_analysis.md")
    
    return analysis

# Usage
papers = ['paper1.pdf', 'paper2.pdf', 'paper3.pdf']
gaps = find_research_gaps(papers)