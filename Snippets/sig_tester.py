"""
Title: Result Significance Tester
Subtitle: LLM checks statistical significance
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: LLM, Statistics, Significance, Analysis
"""

from langchain.llms import Ollama
import pandas as pd

def check_result_significance(results: dict, baseline: dict):
    """Check if improvement is significant"""
    
    llm = Ollama(model="llama2", temperature=0.1)
    
    prompt = f"""Analyze if this improvement is statistically significant:

Our model: {results}
Baseline: {baseline}

Consider:
1. Magnitude of improvement
2. Whether standard error/confidence intervals overlap
3. Practical significance
4. Statistical tests needed

Provide:
- Is improvement significant? (Yes/No/Uncertain)
- Explanation
- Recommended statistical test
- What additional data is needed

Analysis:"""
    
    analysis = llm(prompt)
    
    print("Statistical Significance Analysis:")
    print("="*50)
    print(analysis)
    
    return analysis

def suggest_statistical_test(experiment_design: str):
    """Suggest appropriate statistical test"""
    
    llm = Ollama(model="llama2", temperature=0.2)
    
    prompt = f"""Suggest appropriate statistical test:

Experiment design: {experiment_design}

Recommend:
1. Statistical test to use
2. Why this test is appropriate
3. Assumptions to check
4. How to report results

Recommendation:"""
    
    recommendation = llm(prompt)
    
    return recommendation

# Usage
results = {
    'accuracy': 0.94,
    'f1_score': 0.92,
    'n_samples': 1000
}

baseline = {
    'accuracy': 0.89,
    'f1_score': 0.87,
    'n_samples': 1000
}

check_result_significance(results, baseline)

# Suggest test
design = "Comparing two models on same dataset, independent samples"
test = suggest_statistical_test(design)
print("\n" + test)