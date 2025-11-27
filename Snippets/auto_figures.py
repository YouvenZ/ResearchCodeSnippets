"""
Title: Auto Figure Inclusion
Subtitle: Scan folder and add all figures to LaTeX
Date: 2024-11-24
Category: Academic Writing
Difficulty: Beginner
Tags: LaTeX, Figures, Automation, Inclusion
"""

from pathlib import Path

def generate_figures_latex(figures_dir: str = './figures'):
    """Generate LaTeX code for all figures in directory"""
    
    figure_files = list(Path(figures_dir).glob('*.pdf')) + \
                   list(Path(figures_dir).glob('*.png'))
    
    latex_code = ""
    
    for idx, fig_path in enumerate(sorted(figure_files), 1):
        fig_name = fig_path.stem
        
        # Generate caption from filename (snake_case to Title Case)
        caption = fig_name.replace('_', ' ').title()
        
        latex_code += f"""\\begin{{figure}}[htbp]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{fig_path.relative_to('.')}}}
\\caption{{{caption}}}
\\label{{fig:{fig_name}}}
\\end{{figure}}

"""
    
    # Save to file
    with open('figures.tex', 'w') as f:
        f.write(latex_code)
    
    print(f"✓ Generated LaTeX for {len(figure_files)} figures")
    print("✓ Saved to figures.tex")
    print("📝 Include in main paper: \\input{figures}")
    
    # Also generate list for easy reference
    ref_list = [f"\\ref{{fig:{f.stem}}}" for f in figure_files]
    print(f"\n📊 Figure references: {', '.join(ref_list)}")
    
    return latex_code

# Usage - organize figures in ./figures/ directory
# Files: accuracy_plot.pdf, confusion_matrix.png, etc.

generate_figures_latex('../../mermaid-images/')