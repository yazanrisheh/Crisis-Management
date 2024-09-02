import streamlit as st
import time
from crewai import Crew, Process
from agents import search_agent, analysis_agent, volunteer_matcher_agent
from tasks import search_task, analysis_task, volunteer_matching_task

# Streamlit app title
st.title("Crisis Management Crew")

# User input for the crisis name
crisis_name = st.text_input("Enter the name of the crisis:", "")

# Button to kick off the crew process
if st.button("Start Research"):
    if crisis_name:
        st.write(f"Initiating the research process for: {crisis_name}")

        # Forming the crew
        crew = Crew(
            agents=[search_agent, analysis_agent, volunteer_matcher_agent],
            tasks=[search_task, analysis_task, volunteer_matching_task],
            process=Process.sequential
        )

        # Start the process
        start_time = time.time()
        result = crew.kickoff(inputs={'crisis': crisis_name})
        end_time = time.time()

        # Display the results
        st.subheader("Results")
        st.write(result)

        # Display the time taken
        total_time = end_time - start_time
        st.subheader("Time Taken")
        st.write(f"{total_time:.2f} seconds")
    else:
        st.write("Please enter a crisis name before starting the research.")
