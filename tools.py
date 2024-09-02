from crewai_tools import SerperDevTool, CSVSearchTool

# Search tool for the Internet Researcher
search_tool = SerperDevTool(n_results=5)

# CSV search tool for the Volunteer Matcher
csv_search_tool = CSVSearchTool(csv=r'C:\Users\Asus\Documents\Hajer\volunteers.csv')
