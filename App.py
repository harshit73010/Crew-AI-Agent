__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')    
import os
import streamlit as st

from crewai import Agent, Task, Crew, LLM

# API KEY
api_key=st.secrets["api_key"]
os.environ["GROQ_API_KEY"] = api_key

# LLM
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.environ["GROQ_API_KEY"]
)
# Page config
st.set_page_config(page_title="Crew Mind Agent", page_icon="🤖")

# Title
st.title("🤖 Crew Mind Agent")
st.write("Powered by Harshit 🚀")

# Streamlit UI
#st.title("Crew Mind Agent")

query = st.text_input("Enter your research topic")

if st.button("Run Agent"):

    researcher = Agent(
        role="Project manager",
        goal=f"Write {query}",
        backstory="You are an expert project manager.",
        llm=llm
    )

    task = Task(
        description=f"detailed writing {query}",
        expected_output="A detailed report",
        agent=researcher
    )

    crew = Crew(
        agents=[researcher],
        tasks=[task]
    )

    result = crew.kickoff()

    st.markdown(result.raw)
