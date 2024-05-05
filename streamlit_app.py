import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os

st.title('Research Crew Setup')
os.environ["OPENAI_API_KEY"] = "YOU API KEY HERE"
os.environ["SERPER_API_KEY"] = "YOU API KEY HERE"

with st.sidebar:
    st.header('Enter Research Details')
    topic = st.text_input("Main topic of your research:")
    detailed_questions = st.text_area("Specific questions or subtopics you are interested in exploring:")
    key_points = st.text_area("Key points or specific information needed:")

if st.button('Run Research'):
    if not topic or not detailed_questions or not key_points:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Research Topic: {topic}\nDetailed Questions: {detailed_questions}\nKey Points: {key_points}"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Results of your research project:")
        st.write(result)
