"""
Title: Abstract Generator from Results
Subtitle: LLM creates abstract from your data
Date: 2024-11-24
Category: AI Tools
Difficulty: Beginner
Tags: LLM, Abstract, Writing, Automation
"""

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

def generate_abstract(title: str, methods: str, results: dict):
    """Generate paper abstract using LLM"""
    
    # Setup local LLM
    llm = Ollama(model="llama2", temperature=0.7)
    
    # Create prompt template
    template = """Write a structured academic abstract for a research paper:

Title: {title}

Methodology: {methods}

Key Results:
{results}

Generate a 200-word abstract with:
1. Background (1-2 sentences)
2. Methods (2-3 sentences)
3. Results (2-3 sentences)
4. Conclusion (1-2 sentences)

Abstract:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["title", "methods", "results"]
    )
    
    # Format results
    results_text = "\n".join([f"- {k}: {v}" for k, v in results.items()])
    
    # Generate abstract
    abstract = llm(prompt.format(
        title=title,
        methods=methods,
        results=results_text
    ))
    
    print("✓ Generated abstract:")
    print(abstract)
    
    return abstract

# Usage
abstract = generate_abstract(
    title="Novel Deep Learning Approach for Text Classification",
    methods="Transformer-based architecture with attention mechanism",
    results={
        "Accuracy": "94.5% on test set",
        "F1-Score": "0.93 (macro average)",
        "Improvement": "5% over SOTA baseline"
    }
)