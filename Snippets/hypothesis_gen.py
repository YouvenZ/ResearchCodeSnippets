"""
Title: Auto Hypothesis Generator
Subtitle: LLM suggests research hypotheses
Date: 2024-11-24
Category: AI Tools
Difficulty: Beginner
Tags: LLM, Hypothesis, Research, Ideas
"""

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

def generate_hypotheses(research_area: str, context: str, n: int = 5):
    """Generate research hypotheses using LLM"""
    
    llm = Ollama(model="llama2", temperature=0.9)
    
    template = """You are a creative research scientist.

Research Area: {area}

Context and Background:
{context}

Generate {n} novel, testable research hypotheses for this area.
Each hypothesis should be:
1. Specific and measurable
2. Based on the context
3. Scientifically rigorous
4. Potentially impactful

Format:
H1: [hypothesis]
Rationale: [why this is interesting]

Hypotheses:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["area", "context", "n"]
    )
    
    hypotheses = llm(prompt.format(
        area=research_area,
        context=context,
        n=n
    ))
    
    print(f"💡 Generated {n} hypotheses:\n")
    print(hypotheses)
    
    return hypotheses

# Usage
hypotheses = generate_hypotheses(
    research_area="Natural Language Processing",
    context="""Recent work shows that large language models can perform 
    few-shot learning. However, they struggle with numerical reasoning 
    and require massive computational resources.""",
    n=3
)