"""
Title: Confusion Matrix Pretty
Subtitle: Beautiful confusion matrices for papers
Date: 2024-11-24
Category: Visualization
Difficulty: Beginner
Tags: ConfusionMatrix, Visualization, Classification, Metrics
"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
    """Create publication-ready confusion matrix"""
    
    cm = confusion_matrix(y_true, y_pred)
    
    # Calculate percentages
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, None] * 100
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create heatmap with both counts and percentages
    sns.heatmap(cm, annot=False, fmt='d', cmap='Blues', 
                square=True, cbar_kws={'label': 'Count'}, ax=ax)
    
    # Add custom annotations with count and percentage
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            text = f'{cm[i,j]}\n({cm_percent[i,j]:.1f}%)'
            ax.text(j+0.5, i+0.5, text, ha='center', va='center')
    
    if labels:
        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)
    
    ax.set_ylabel('True Label', fontsize=12)
    ax.set_xlabel('Predicted Label', fontsize=12)
    ax.set_title('Confusion Matrix', fontsize=14, pad=20)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

# Usage
y_true = [0, 1, 2, 1, 0, 2, 1, 0]
y_pred = [0, 2, 2, 1, 0, 2, 1, 1]
plot_confusion_matrix(y_true, y_pred, labels=['A', 'B', 'C'])