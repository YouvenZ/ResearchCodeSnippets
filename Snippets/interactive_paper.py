"""
Title: Interactive Paper Builder
Subtitle: Chat with AI to write your paper
Date: 2024-11-24
Category: AI Tools
Difficulty: Intermediate
Tags: Chatbot, Interactive, Writing, LLM
"""

from langchain.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

class InteractivePaperWriter:
    def __init__(self):
        self.llm = Ollama(model="llama2", temperature=0.7)
        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(llm=self.llm, memory=self.memory)
        
        self.sections = {}
        
        print("📝 Interactive Paper Writer")
        print("=" * 50)
        print("I'll help you write your paper section by section.")
        print("Commands: write <section>, review <section>, save, quit\n")
    
    def write_section(self, section: str):
        """Collaboratively write a section"""
        print(f"\n📄 Writing {section} section...")
        print("Tell me about this section (or 'done' to finish):\n")
        
        context = []
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'done':
                break
            context.append(user_input)
        
        # Generate section
        prompt = f"""Based on this information, write the {section} section:

{chr(10).join(context)}

Write in academic style, clear and concise."""
        
        section_text = self.chain.predict(input=prompt)
        self.sections[section] = section_text
        
        print(f"\n{section}:\n{section_text}\n")
        
        # Offer revision
        revise = input("Revise? (yes/no): ")
        if revise.lower() == 'yes':
            feedback = input("What to change: ")
            revised = self.chain.predict(
                input=f"Revise this based on feedback:\n\n{section_text}\n\nFeedback: {feedback}"
            )
            self.sections[section] = revised
            print(f"\nRevised:\n{revised}\n")
    
    def save_paper(self):
        """Save complete paper"""
        paper = ""
        for section, content in self.sections.items():
            paper += f"# {section}\n\n{content}\n\n"
        
        with open('draft_paper.md', 'w') as f:
            f.write(paper)
        
        print("✅ Saved to draft_paper.md")
    
    def run(self):
        """Interactive loop"""
        while True:
            command = input("\nCommand: ").strip().lower()
            
            if command.startswith('write '):
                section = command.replace('write ', '')
                self.write_section(section)
            elif command.startswith('review '):
                section = command.replace('review ', '')
                if section in self.sections:
                    print(f"\n{section}:\n{self.sections[section]}\n")
            elif command == 'save':
                self.save_paper()
            elif command == 'quit':
                break

# Usage
writer = InteractivePaperWriter()
writer.run()