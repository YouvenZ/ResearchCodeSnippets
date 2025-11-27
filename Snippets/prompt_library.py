"""
Title: Smart Prompt Library
Subtitle: Reusable research prompts with RAG
Date: 2024-11-24
Category: AI Tools
Difficulty: Beginner
Tags: Prompts, LLM, Library, Reusable
"""

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
import json

class ResearchPromptLibrary:
    def __init__(self):
        self.llm = Ollama(model="llama2")
        self.prompts = {
            'summarize': """Summarize this research text in 3 bullet points:
{text}
Summary:""",
            
            'critique': """Critically evaluate this claim:
{text}
Strengths:
Weaknesses:
Verdict:""",
            
            'expand': """Expand on this research idea with 3 concrete examples:
{text}
Examples:""",
            
            'simplify': """Explain this technical concept to non-experts:
{text}
Simple explanation:""",
            
            'methodology': """Suggest 3 methods to test this hypothesis:
{text}
Methods:"""
        }
    
    def apply(self, prompt_name: str, text: str):
        """Apply prompt template to text"""
        template = self.prompts.get(prompt_name)
        if not template:
            return "Prompt not found"
        
        prompt = PromptTemplate(template=template, input_variables=["text"])
        return self.llm(prompt.format(text=text))
    
    def add_custom(self, name: str, template: str):
        """Add custom prompt"""
        self.prompts[name] = template
        self._save_prompts()
    
    def _save_prompts(self):
        with open('prompt_library.json', 'w') as f:
            json.dump(self.prompts, f, indent=2)

# Usage
lib = ResearchPromptLibrary()

text = "Transformers use self-attention mechanisms for sequence modeling."
summary = lib.apply('summarize', text)
simple = lib.apply('simplify', text)

print("Summary:", summary)
print("\nSimple:", simple)