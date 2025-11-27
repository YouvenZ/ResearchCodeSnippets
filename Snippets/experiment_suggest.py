"""
Title: Smart Experiment Suggester
Subtitle: AI recommends next experiments
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: LLM, Experiments, Planning, Agent
"""

from langchain.llms import Ollama
import json

def suggest_next_experiments(previous_results: list, goal: str):
    """AI suggests next experiments based on results"""
    
    llm = Ollama(model="llama2", temperature=0.8)
    
    # Format previous results
    results_summary = "\n".join([
        f"- {r['name']}: {r['metric']} = {r['value']:.3f}"
        for r in previous_results
    ])
    
    prompt = f"""You are an AI research assistant helping design experiments.

Research Goal: {goal}

Previous Experiment Results:
{results_summary}

Based on these results, suggest 3 promising experiments to try next.
For each experiment, provide:
1. Hypothesis (what you expect)
2. Methodology (what to change)
3. Success criteria (how to evaluate)
4. Risk assessment (potential issues)

Suggestions:"""
    
    suggestions = llm(prompt)
    
    print("🔬 Suggested Next Experiments:\n")
    print(suggestions)
    
    # Save to file
    with open('experiment_suggestions.md', 'w') as f:
        f.write(f"# Experiment Suggestions\n\n")
        f.write(f"**Goal**: {goal}\n\n")
        f.write(suggestions)
    
    return suggestions

# Usage
results = [
    {'name': 'Baseline', 'metric': 'accuracy', 'value': 0.85},
    {'name': 'Added Dropout', 'metric': 'accuracy', 'value': 0.87},
    {'name': 'Increased Depth', 'metric': 'accuracy', 'value': 0.83}
]

suggestions = suggest_next_experiments(
    results, 
    goal="Improve model accuracy above 0.90 while maintaining efficiency"
)