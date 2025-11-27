"""
Title: LaTeX Table from DataFrame
Subtitle: Publication-ready tables in one line
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: LaTeX, Tables, Pandas, Formatting
"""

import pandas as pd

def df_to_publication_table(df: pd.DataFrame, caption: str, 
                            label: str, highlight_best: bool = True):
    """Create publication-ready LaTeX table with formatting"""
    
    df_copy = df.copy()
    
    # Format numeric columns
    for col in df_copy.select_dtypes(include=['float']).columns:
        # Highlight best value if requested
        if highlight_best:
            best_idx = df_copy[col].idxmax()
            df_copy[col] = df_copy[col].apply(lambda x: f"{x:.3f}")
            df_copy.loc[best_idx, col] = f"\\textbf{{{df_copy.loc[best_idx, col]}}}"
        else:
            df_copy[col] = df_copy[col].apply(lambda x: f"{x:.3f}")
    
    # Generate LaTeX
    latex = df_copy.to_latex(
        index=False,
        escape=False,
        column_format='l' + 'c' * (len(df.columns) - 1)
    )
    
    # Wrap in table environment with caption
    full_table = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{{caption}}}
\\label{{{label}}}
{latex}
\\end{{table}}
"""
    
    # Save
    with open(f'{label}.tex', 'w') as f:
        f.write(full_table)
    
    print(f"✓ Created {label}.tex")
    print(f"📝 Include in paper: \\input{{{label}}}")
    
    return full_table

# Usage
results = pd.DataFrame({
    'Model': ['BERT', 'GPT-2', 'T5', 'Ours'],
    'Accuracy': [0.891, 0.876, 0.903, 0.924],
    'F1-Score': [0.867, 0.854, 0.889, 0.912],
    'Speed (ms)': [45, 38, 52, 41]
})

df_to_publication_table(
    results,
    caption='Comparison of model performance',
    label='tab:results',
    highlight_best=True
)