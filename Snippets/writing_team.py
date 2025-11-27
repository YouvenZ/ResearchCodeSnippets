"""
Title: Multi-Agent Writing Team
Subtitle: Specialized agents write paper sections
Date: 2024-11-24
Category: AI Tools
Difficulty: Advanced
Tags: MultiAgent, CrewAI, Writing, Collaboration
"""

from crewai import Agent, Task, Crew
from langchain.llms import Ollama

def create_writing_team(research_data: dict):
    """Create specialized agents for paper writing"""
    
    llm = Ollama(model="llama2")
    
    # Specialized writing agents
    intro_writer = Agent(
        role='Introduction Specialist',
        goal='Write compelling introductions with clear motivation',
        backstory='Expert at framing research problems and contributions',
        llm=llm
    )
    
    methods_writer = Agent(
        role='Methods Expert',
        goal='Explain methodology clearly and reproducibly',
        backstory='Technical writer with deep understanding of research methods',
        llm=llm
    )
    
    results_writer = Agent(
        role='Results Analyst',
        goal='Present findings clearly with proper statistics',
        backstory='Data scientist skilled at communicating results',
        llm=llm
    )
    
    editor = Agent(
        role='Academic Editor',
        goal='Ensure coherence and academic quality',
        backstory='Published author who polishes manuscripts',
        llm=llm
    )
    
    # Define writing tasks
    intro_task = Task(
        description=f"""Write Introduction section covering:
        - Problem: {research_data['problem']}
        - Gap: {research_data['gap']}
        - Contribution: {research_data['contribution']}
        Make it compelling and clear.""",
        agent=intro_writer,
        expected_output='2-3 paragraph introduction'
    )
    
    methods_task = Task(
        description=f"""Write Methods section explaining:
        - Approach: {research_data['approach']}
        - Implementation: {research_data['implementation']}
        Make it reproducible.""",
        agent=methods_writer,
        expected_output='Detailed methodology description'
    )
    
    results_task = Task(
        description=f"""Write Results section presenting:
        - Findings: {research_data['results']}
        Include statistical analysis.""",
        agent=results_writer,
        expected_output='Results with analysis'
    )
    
    edit_task = Task(
        description='Review and polish all sections for coherence',
        agent=editor,
        expected_output='Edited complete draft'
    )
    
    # Create crew
    crew = Crew(
        agents=[intro_writer, methods_writer, results_writer, editor],
        tasks=[intro_task, methods_task, results_task, edit_task],
        verbose=True
    )
    
    return crew

# Usage
data = {
    'problem': 'Current NLP models are computationally expensive',
    'gap': 'No efficient alternative maintains accuracy',
    'contribution': 'Novel architecture 50% faster with same accuracy',
    'approach': 'Sparse attention mechanism',
    'implementation': 'PyTorch with custom CUDA kernels',
    'results': 'Accuracy: 94.5%, Speed: 2x faster'
}

team = create_writing_team(data)
draft = team.kickoff()
print(draft)