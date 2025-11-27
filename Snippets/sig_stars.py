"""
Title: Significance Stars Helper
Subtitle: Add p-value stars to tables automatically
Date: 2024-11-24
Category: Statistics
Difficulty: Beginner
Tags: Statistics, PValues, Tables, Formatting
"""

import pandas as pd

def add_significance_stars(df: pd.DataFrame, p_col: str) -> pd.DataFrame:
    """Add significance stars based on p-values"""
    
    def get_stars(p):
        if p < 0.001:
            return '***'
        elif p < 0.01:
            return '**'
        elif p < 0.05:
            return '*'
        else:
            return 'ns'
    
    df = df.copy()
    df['Sig.'] = df[p_col].apply(get_stars)
    
    # Format p-values nicely
    df[p_col] = df[p_col].apply(lambda x: f'{x:.4f}' if x >= 0.001 else '<0.001')
    
    return df

def format_results_table(df: pd.DataFrame, metric_cols: list, p_col: str):
    """Format results table with mean±std and significance"""
    
    # Add stars
    df = add_significance_stars(df, p_col)
    
    # Round metrics
    for col in metric_cols:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: f'{x:.3f}')
    
    return df

# Usage
results = pd.DataFrame({
    'Method': ['Baseline', 'Our Method', 'SOTA'],
    'Accuracy': [0.856, 0.923, 0.891],
    'F1': [0.841, 0.915, 0.878],
    'p_value': [1.0, 0.003, 0.021]
})

formatted = format_results_table(results, ['Accuracy', 'F1'], 'p_value')
print(formatted.to_latex(index=False))