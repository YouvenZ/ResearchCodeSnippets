"""
Title: Paper Reviewer Agent
Subtitle: AI reviews your paper before submission
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: Agent, Review, Quality, Feedback
"""

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

def review_paper_section(text: str, section_type: str):
    """AI reviews paper section with specific criteria"""
    
    llm = Ollama(model="llama2", temperature=0.3)
    
    criteria = {
        'abstract': ['completeness', 'clarity', 'structure', 'keywords'],
        'introduction': ['motivation', 'background', 'contribution', 'organization'],
        'methods': ['reproducibility', 'clarity', 'justification', 'detail'],
        'results': ['clarity', 'completeness', 'statistical_rigor', 'visualization'],
        'conclusion': ['summary', 'implications', 'limitations', 'future_work']
    }
    
    template = """You are an expert paper reviewer. Review this {section} section:

{text}

Evaluate based on:
{criteria}

Provide:
1. Overall score (1-5)
2. Strengths (2-3 points)
3. Weaknesses (2-3 points)
4. Specific suggestions for improvement

Review:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["section", "text", "criteria"]
    )
    
    review = llm(prompt.format(
        section=section_type,
        text=text[:2000],
        criteria='\n'.join([f"- {c}" for c in criteria.get(section_type, [])])
    ))
    
    return review

# Usage
abstract = """Deep learning has transformed NLP. We propose a novel architecture
that achieves state-of-the-art results on multiple benchmarks."""

review = review_paper_section(abstract, 'abstract')
print("📝 Review:\n")
print(review)