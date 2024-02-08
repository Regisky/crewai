from crewai import Agent, Task, Crew, Process
import os
from langchain.llms import Ollama
ollama_oppenhermes = Ollama(model="openhermes")

researcher = A
    role = 'Researcher',
    goal = 'develop ideas for teaching someone new to the subject',
    backstory = 'you are an ai research assistant',
    verbose = True,
    allow_delegation = False,
    llm = ollama_oppenhermes
    )
writer = Agent(
        role = 'Writer',
        goal = 'use the researchers ideas to write a piece of text to explain the topic',
        backstory = 'you are an ai research assistant',
        verbose = True,
        allow_delegation = False,
        llm = ollama_oppenhermes
        )
examiner = Agent(
    role = 'Examiner',
    goal = 'Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers',
    backstory = 'you are an ai research assistant',
    verbose = True,
    allow_delegation = False,
    llm = ollama_oppenhermes
    )

task1 = Task(description= 'Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers', agent=examiner)

crew = Crew(
    agents= [researcher, writer, examiner],
    task = [task1],
    llm = ollama_oppenhermes,
    verbose = 2 ,
    process = Process.sequential
    )

result = crew.kickoff()
print(result)