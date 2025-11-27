"""
Title: Publication-Ready Plots
Subtitle: Scientific matplotlib configurations
Date: 2024-11-24
Category: Data Visualization
Difficulty: Intermediate
Tags: Matplotlib, Visualization, Scientific, Publication
"""

import matplotlib.pyplot as plt
import numpy as np

# Publication settings
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'lines.linewidth': 2
})

def create_publication_figure(data, xlabel, ylabel, title):
    """Create publication-quality figure"""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    ax.plot(data['x'], data['y'], 'o-', label='Results')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(frameon=True, fancybox=True, shadow=True)
    
    plt.tight_layout()
    return fig

# Save for publication
fig = create_publication_figure(
    {'x': np.arange(10), 'y': np.random.randn(10).cumsum()},
    'Time (s)', 'Accuracy (%)', 'Model Performance'
)
fig.savefig('figure1.pdf', format='pdf')