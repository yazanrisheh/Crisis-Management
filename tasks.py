from crewai import Task
from agents import search_agent, analysis_agent, volunteer_matcher_agent
from tools import csv_search_tool

# Search Task
search_task = Task(
    description=(
        "Search for and retrieve detailed information about a crisis. "
        "Ensure the information is comprehensive and covers the crisis's "
        "description, type, date, location, and any other relevant details."
    ),
    expected_output='A detailed report of the crisis information.',
    tools=[],
    agent=search_agent
)

# Analysis Task
analysis_task = Task(
    description=(
        "Analyze the information gathered by the Search Agent and break it down "
        "into the following components:\n"
        "1) Description of the crisis\n"
        "2) Type of crisis (e.g., flood, earthquake)\n"
        "3) Date of the crisis\n"
        "4) Location of the crisis\n"
        "5) Skills required by volunteers"
    ),
    expected_output='A structured report detailing the crisis as per the specified components.',
    tools=[],
    agent=analysis_agent,
    context = [search_task]
)

# Volunteer Matching Task
volunteer_matching_task = Task(
    description=(
        "Match the skills required with volunteers from the CSV file and provide their contact information in the following format:\n"
        "Name\n"
        "Phone Number\n"
        "Email\n"
        "Age\n"
        "Skills"
    ),
    expected_output='Contact information of three suitable volunteers in the specified format.',
    tools=[csv_search_tool],
    agent=volunteer_matcher_agent,
    context = [analysis_task]
)
