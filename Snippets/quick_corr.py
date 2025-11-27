"""
Title: Quick Correlation Plot
Subtitle: Visualize correlations in 2 lines
Date: 2024-11-24
Category: Visualization
Difficulty: Beginner
Tags: Correlation, Visualization, Seaborn, Quick
"""

import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation(df, save_path=None):
    """Create correlation heatmap quickly"""
    
    # Calculate correlations
    corr = df.corr()
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, square=True, linewidths=1)
    
    plt.title('Correlation Matrix', fontsize=14, pad=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return corr

# Usage
import pandas as pd
df = pd.read_csv('data.csv')
corr = plot_correlation(df, 'correlation.pdf')

# Find strong correlations
strong = corr[abs(corr) > 0.7].stack().drop_duplicates()
print(f"Found {len(strong)} strong correlations")