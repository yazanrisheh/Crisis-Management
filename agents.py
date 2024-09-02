from crewai import Agent
from tools import search_tool, csv_search_tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature = 0.3, model = "gpt-4o-mini")
# llm = ChatGroq(temperature=0.3, model = "Llama-3.1-8b-Instant")

# Search Agent
search_agent = Agent(
    role='Senior Crisis Internet Researcher',
    goal='To search for information about a specific crisis on the internet provided to you.',
    backstory="""A seasoned researcher with extensive experience in researching and finding facts and relevant information
    about crisis events happening around the world.""",
    tools=[search_tool],
    verbose=True,
    llm = llm
)

# Analysis Agent
analysis_agent = Agent(
    role='Senior Crisis Analyst',
    goal='To analyze the information gathered and break it down into actionable insights.',
    backstory="""
    An expert analyst in breaking down complex crisis situations into actionable insights, ensuring all relevant details are 
    captured. The output is in the form of a structured report:
    1) Description about the crisis
    2) Type of the crisis (like flood or earthquake etc..)
    3) Date of the crisis
    4) Location of the crisis
    5) Skills required by volunteers to assist during this crisis
    """,
    tools=[],
    verbose=True,
    llm = llm
)

# Volunteer Matcher Agent
volunteer_matcher_agent = Agent(
    role='Volunteer Coordinator',
    goal='To find and match volunteers based on the skills required for the crisis.',
    backstory='Highly skilled at connecting the right people with the right tasks, ensuring efficient and effective crisis response.',
    tools=[csv_search_tool],
    verbose=True,
    llm = llm
)