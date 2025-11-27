"""
Title: Dataset Statistics Report
Subtitle: Generate dataset overview automatically
Date: 2024-11-24
Category: Data Science
Difficulty: Beginner
Tags: Dataset, Statistics, Report, Analysis
"""

import pandas as pd
import numpy as np

def generate_dataset_report(df: pd.DataFrame, target_col: str = None):
    """Generate comprehensive dataset statistics"""
    
    report = f"""# Dataset Report

## Overview
- **Samples**: {len(df):,}
- **Features**: {len(df.columns)}
- **Memory**: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB

## Feature Types
"""
    
    # Count feature types
    numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical = df.select_dtypes(include=['object']).columns.tolist()
    
    report += f"- Numeric: {len(numeric)}\n"
    report += f"- Categorical: {len(categorical)}\n\n"
    
    # Missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        report += "## Missing Values\n"
        for col, count in missing[missing > 0].items():
            pct = count / len(df) * 100
            report += f"- {col}: {count} ({pct:.1f}%)\n"
    
    # Target distribution (if provided)
    if target_col and target_col in df.columns:
        report += f"\n## Target Distribution ({target_col})\n"
        counts = df[target_col].value_counts()
        for val, count in counts.items():
            pct = count / len(df) * 100
            report += f"- {val}: {count} ({pct:.1f}%)\n"
    
    # Save report
    with open('dataset_report.md', 'w') as f:
        f.write(report)
    
    print("✓ Report saved to dataset_report.md")
    return report

# Usage
df = pd.read_csv('data.csv')
report = generate_dataset_report(df, target_col='label')
print(report)