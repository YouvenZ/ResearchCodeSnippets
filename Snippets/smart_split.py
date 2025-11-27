"""
Title: Smart Train-Test Split
Subtitle: Stratified split with visualization
Date: 2024-11-24
Category: Machine Learning
Difficulty: Beginner
Tags: TrainTest, Split, Stratified, Visualization
"""

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

def smart_split(X, y, test_size=0.2, random_state=42, visualize=True):
    """Stratified split with distribution check"""
    
    # Perform stratified split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, 
        stratify=y
    )
    
    print(f"✓ Train: {len(X_train)} samples")
    print(f"✓ Test: {len(X_test)} samples")
    
    if visualize:
        # Compare distributions
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Train distribution
        pd.Series(y_train).value_counts().plot(kind='bar', ax=ax1, 
                                               title='Train Distribution')
        
        # Test distribution
        pd.Series(y_test).value_counts().plot(kind='bar', ax=ax2,
                                              title='Test Distribution')
        
        plt.tight_layout()
        plt.savefig('split_distribution.pdf', dpi=300, bbox_inches='tight')
        print("✓ Saved split_distribution.pdf")
    
    return X_train, X_test, y_train, y_test

# Usage
import numpy as np
X = np.random.randn(1000, 10)
y = np.random.choice(['A', 'B', 'C'], 1000)

X_train, X_test, y_train, y_test = smart_split(X, y, visualize=True)