"""
Title: CSV to LaTeX Tables
Subtitle: Professional academic tables in seconds
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: LaTeX, CSV, Tables, Academic
"""

import pandas as pd

def csv_to_latex_table(csv_path: str, caption: str = None, 
                       label: str = None, bold_max: bool = True):
    """Convert CSV to beautiful LaTeX table"""
    
    df = pd.read_csv(csv_path)
    
    # Bold maximum values in each numeric column
    if bold_max:
        for col in df.select_dtypes(include=['float', 'int']).columns:
            max_val = df[col].max()
            df[col] = df[col].apply(
                lambda x: f'\\textbf{{{x}}}' if x == max_val else x
            )
    
    # Generate LaTeX
    latex = df.to_latex(
        index=False,
        escape=False,
        column_format='l' + 'c' * (len(df.columns) - 1),
        caption=caption,
        label=label,
        position='htbp'
    )
    
    # Add booktabs for professional look
    latex = latex.replace('\\toprule', '\\toprule\n')
    latex = latex.replace('\\midrule', '\\midrule\n')
    
    return latex

# Usage
table = csv_to_latex_table(
    'results.csv',
    caption='Experimental Results',
    label='tab:results'
)
print(table)