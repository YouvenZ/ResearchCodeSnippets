"""
Title: Code-to-Method Explainer
Subtitle: LLM documents your research code
Date: 2024-11-24
Category: AI Tools
Difficulty: Beginner
Tags: LLM, Code, Documentation, Methods
"""

from langchain.llms import Ollama
import ast

def explain_code_for_paper(code_file: str):
    """Generate Methods section from research code"""
    
    llm = Ollama(model="codellama")
    
    # Read code
    with open(code_file, 'r') as f:
        code = f.read()
    
    # Parse to find main functions
    tree = ast.parse(code)
    functions = [node.name for node in ast.walk(tree) 
                 if isinstance(node, ast.FunctionDef)]
    
    prompt = f"""Analyze this research code and write a Methods section:

```python
{code[:2000]}  # First 2000 chars
```

Main functions: {', '.join(functions)}

Write a clear Methods section explaining:
1. Overall approach
2. Key algorithms used
3. Implementation details
4. Parameters and hyperparameters

Use formal academic language suitable for a research paper.

Methods Section:"""
    
    explanation = llm(prompt)
    
    with open('methods_from_code.tex', 'w') as f:
        f.write("\\section{Methodology}\n\n")
        f.write(explanation)
    
    print("✓ Generated methods_from_code.tex")
    return explanation

# Usage
explanation = explain_code_for_paper('model.py')
print(explanation[:300] + "...")