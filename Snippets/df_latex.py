"""
Title: DataFrame to LaTeX
Subtitle: One-line table conversion
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: Pandas, LaTeX, Tables, Quick
"""

import pandas as pd

def df_to_latex_quick(df, caption="Results", label="tab:results"):
    """Convert DataFrame to LaTeX table quickly"""
    
    latex = df.to_latex(
        index=False,
        float_format="%.3f",
        caption=caption,
        label=label,
        position='htbp',
        column_format='l' + 'c' * (len(df.columns) - 1)
    )
    
    # Add booktabs for professional look
    latex = latex.replace('\\toprule', '\\toprule\n').replace(
        '\\bottomrule', '\n\\bottomrule'
    )
    
    return latex

# Usage
df = pd.DataFrame({
    'Model': ['BERT', 'GPT', 'T5'],
    'Accuracy': [0.92, 0.89, 0.94],
    'F1': [0.90, 0.87, 0.93]
})

print(df_to_latex_quick(df, "Model Comparison"))