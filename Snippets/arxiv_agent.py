"""
Title: ArXiv Research Agent
Subtitle: Automated paper search with CrewAI
Date: 2024-11-24
Category: AI Research
Difficulty: Advanced
Tags: CrewAI, ArXiv, Research, AI
"""

from crewai import Agent, Task, Crew
import arxiv

# Define ArXiv search agent
arxiv_agent = Agent(
    role='Research Assistant',
    goal='Find and summarize recent papers on {topic}',
    backstory='Expert in academic literature search',
    verbose=True
)

# Create search task
def search_arxiv(query: str, max_results: int = 5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'authors': [a.name for a in result.authors],
            'summary': result.summary[:300],
            'pdf_url': result.pdf_url,
            'published': result.published.date()
        })
    return papers

# Define task
research_task = Task(
    description='Search ArXiv for papers on {topic}',
    agent=arxiv_agent,
    expected_output='List of relevant papers with summaries'
)

# Execute
crew = Crew(agents=[arxiv_agent], tasks=[research_task])
result = crew.kickoff(inputs={'topic': 'transformer models'})