"""
Title: Statistical Reporting
Subtitle: Generate LaTeX statistical summaries
Date: 2024-11-24
Category: Statistics
Difficulty: Intermediate
Tags: Statistics, LaTeX, Reporting, Analysis
"""

import pandas as pd
import numpy as np
from scipy import stats

def generate_stats_report(df: pd.DataFrame, 
                         group_col: str = None) -> str:
    """Generate LaTeX statistical report"""
    
    report = []
    report.append("\\begin{table}[htbp]")
    report.append("\\centering")
    report.append("\\caption{Statistical Summary}")
    
    if group_col:
        # Grouped statistics
        summary = df.groupby(group_col).agg([
            ('Mean', 'mean'),
            ('SD', 'std'),
            ('Median', 'median'),
            ('Min', 'min'),
            ('Max', 'max')
        ])
        
        # Perform ANOVA
        groups = [group for _, group in df.groupby(group_col)]
        f_stat, p_val = stats.f_oneway(*groups)
        
        report.append(f"% ANOVA: F={f_stat:.3f}, p={p_val:.4f}")
    else:
        summary = df.describe().T
    
    # Convert to LaTeX
    latex_table = summary.to_latex(float_format="%.2f")
    report.append(latex_table)
    report.append("\\end{table}")
    
    return "\n".join(report)

# Usage
df = pd.read_csv('experiment_data.csv')
latex_report = generate_stats_report(df, group_col='condition')
print(latex_report)