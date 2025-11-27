"""
Title: Research Question Generator
Subtitle: LLM generates research questions from topic
Author: AI Research
Date: 2024-11-24
Category: AI Tools
Difficulty: Beginner
Tags: LLM, Research, Questions, Planning
"""

from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

def generate_research_questions(topic: str, context: str = ""):
    """Generate research questions for a topic"""
    
    llm = Ollama(model="llama2", temperature=0.8)
    
    template = """You are a research advisor helping formulate research questions.

Topic: {topic}

Context: {context}

Generate 5 research questions that are:
1. Specific and focused
2. Answerable through research
3. Novel and interesting
4. Methodologically feasible
5. Impactful

For each question, also suggest:
- Potential methodology
- Expected contribution
- Key challenges

Research Questions:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["topic", "context"]
    )
    
    questions = llm(prompt.format(topic=topic, context=context))
    
    # Save to file
    with open('research_questions.md', 'w') as f:
        f.write(f"# Research Questions: {topic}\n\n")
        f.write(questions)
    
    print("💡 Generated Research Questions:\n")
    print(questions)
    
    return questions

# Usage
questions = generate_research_questions(
    topic="Efficient Transformers for Mobile Devices",
    context="Current transformers are too large for edge deployment. "
            "There's growing need for on-device AI capabilities."
)