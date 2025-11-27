"""
Title: Compare Model Results
Subtitle: Statistical comparison with effect size
Date: 2024-11-24
Category: Machine Learning
Difficulty: Intermediate
Tags: Statistics, ModelComparison, EffectSize, Analysis
"""

from scipy import stats
import numpy as np

def compare_models(model_a: list, model_b: list):
    """Compare two models with statistical tests"""
    
    # Paired t-test (if same test sets)
    t_stat, p_val = stats.ttest_rel(model_a, model_b)
    
    # Cohen's d (effect size)
    diff = np.array(model_a) - np.array(model_b)
    cohens_d = np.mean(diff) / np.std(diff, ddof=1)
    
    # Interpretation
    if abs(cohens_d) < 0.2:
        effect = "negligible"
    elif abs(cohens_d) < 0.5:
        effect = "small"
    elif abs(cohens_d) < 0.8:
        effect = "medium"
    else:
        effect = "large"
    
    return {
        'p_value': p_val,
        'cohens_d': cohens_d,
        'effect_size': effect,
        'significant': p_val < 0.05,
        'winner': 'Model A' if cohens_d > 0 else 'Model B'
    }

# Usage - compare accuracy across folds
model_a = [0.89, 0.91, 0.90, 0.92, 0.88]
model_b = [0.85, 0.87, 0.86, 0.88, 0.84]

result = compare_models(model_a, model_b)
print(f"Winner: {result['winner']} (d={result['cohens_d']:.2f})")
print(f"Effect: {result['effect_size']}, p={result['p_value']:.4f}")