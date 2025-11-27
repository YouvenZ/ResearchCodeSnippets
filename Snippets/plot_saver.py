"""
Title: Smart Plot Saver
Subtitle: Save plots in all formats at once
Date: 2024-11-24
Category: Visualization
Difficulty: Beginner
Tags: Matplotlib, Export, Formats, Automation
"""

import matplotlib.pyplot as plt

def save_plot_multi(fig, name: str, formats=['pdf', 'png', 'svg']):
    """Save plot in multiple formats for papers"""
    for fmt in formats:
        filename = f"{name}.{fmt}"
        
        # High DPI for PNG
        dpi = 300 if fmt == 'png' else None
        
        fig.savefig(filename, format=fmt, dpi=dpi, 
                   bbox_inches='tight', transparent=True)
        
        print(f"✓ Saved {filename}")

# Usage
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_xlabel('X')
ax.set_ylabel('Y²')

# Save in PDF (LaTeX), PNG (Word), SVG (web)
save_plot_multi(fig, 'figure1')