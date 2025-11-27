"""
Title: SmolaAgent Data Analysis
Subtitle: Intelligent data processing with HF agents
Date: 2024-11-24
Category: Data Science
Difficulty: Intermediate
Tags: SmolaAgent, DataAnalysis, HuggingFace, AI
"""

from smolagents import CodeAgent, HfApiModel
import pandas as pd

# Initialize agent with Hugging Face model
model = HfApiModel(model_id="meta-llama/Llama-3.2-3B-Instruct")
agent = CodeAgent(tools=[], model=model)

# Define data analysis task
def analyze_dataset(df: pd.DataFrame, question: str):
    """Use agent to analyze dataset and answer questions"""
    
    # Provide context to agent
    context = f"""
    Dataset info:
    - Shape: {df.shape}
    - Columns: {df.columns.tolist()}
    - Head:\n{df.head().to_string()}
    
    Question: {question}
    """
    
    response = agent.run(context)
    return response

# Example usage
df = pd.read_csv('research_data.csv')

# Ask intelligent questions
results = analyze_dataset(
    df, 
    "What are the key trends in this data? Provide statistical summary."
)

print(results)