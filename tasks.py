from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Systematically gather and document current and relevant news and articles from diverse sources about {inputs}. Use all available digital tools to ensure comprehensive coverage.",
          expected_output=f"""
  Detailed Research Report on {inputs}
  1. **Executive Summary**: A concise overview of the research findings, highlighting the most critical insights and conclusions drawn from the gathered data.
  2. **Introduction**: Background information on why the research on {inputs} is crucial at this point in time. Include the scope of the research and the main objectives.
  3. **Methodology**:
    - **Sources Used**: List all sources utilized, including digital databases, news websites, and any subscriptions or specialized tools.
    - **Search Criteria**: Describe the search criteria and keywords used to gather the relevant information.
    - **Data Collection Process**: Outline the steps taken in the data collection process, including any automation tools or software used.
  4. **Findings**:
    - **Key Information Gathered**: Summarize the key information gathered from each source, categorized by relevance and impact on the topic.
    - **Themes Identified**: Discuss any recurring themes or commonalities found across different sources.
  5. **Analysis**:
    - **Relevance to Current Trends**: Analyze how the findings relate to current trends or developments in the field.
    - **Gaps in Information**: Highlight any noticeable gaps in information that could require further research.
  6. **Conclusion**:
    - **Summary of Findings**: Briefly reiterate the most critical findings and their implications.
    - **Recommendations for Further Research**: Suggest areas where additional investigation could be beneficial based on gaps or emerging trends noted during the research.
  7. **References**:
    - **Full Citations**: Provide full citations for all sources used, formatted according to a recognized academic standard.
          """
      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description="Critically assess the accuracy, relevance, and depth of the information collected. Employ advanced data analysis methodologies to enhance the information's value, ensuring it meets the high standards required for expert assessment.",
        expected_output=f"""
  Comprehensive Analysis Report:
  1. **Executive Summary**: An overview summarizing the key findings, including the accuracy, relevance, and depth of the analyzed information.
  2. **Accuracy Assessment**:
    - **Data Verification**: Evaluate the truthfulness and correctness of the data collected, identifying any discrepancies or inconsistencies.
    - **Source Reliability**: Assess the reliability of the sources used, providing a credibility score for each.
  3. **Relevance Analysis**:
    - **Contextual Alignment**: Analyze how the information aligns with the current research questions and objectives.
    - **Currentness**: Verify that the information is up-to-date and discuss its significance in the current context.
  4. **Depth Evaluation**:
    - **Comprehensiveness**: Evaluate the scope of the information and whether it covers all necessary aspects of the topic.
    - **Insightfulness**: Assess the depth of insights provided by the information, including any underlying implications or hidden patterns.
  5. **Methodological Review**:
    - **Techniques Used**: Outline and critique the data analysis methodologies employed, suggesting improvements or alternatives if necessary.
    - **Data Handling**: Discuss how the data was processed and analyzed, including any tools or software utilized.
  6. **Recommendations**:
    - **Further Research**: Suggest areas where additional information is needed and propose methods for gathering this data.
    - **Practical Applications**: Provide recommendations on how the findings can be utilized practically by stakeholders or in further research.
  7. **Conclusion**:
    - **Summary of Key Points**: Concisely reiterate the most important findings and their implications for the research project.
    - **Future Directions**: Suggest how the findings can inform future research and decision-making processes in the relevant field.
  8. **Appendices**:
    - **Data Tables and Figures**: Include comprehensive tables, charts, and graphs that were used in the analysis.
    - **Source Documentation**: Provide detailed citations and references for all sources and data used in the report.
          """
    )


    def writing_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Synthesize the information provided by the Researcher and enhanced by the Analyst into a compelling, clear, and well-structured summary. Include key findings and appropriately cite all sources to ensure credibility and traceability.",
            expected_output=f"""
    Comprehensive Summary Report:
    1. **Introduction**:
      - **Background**: Provide a brief introduction to the topic, outlining the scope and purpose of the initial research.
      - **Objectives**: Recap the main objectives of the research to set the context for the findings.

    2. **Synthesis of Research and Analysis**:
      - **Key Findings**: Present the key findings from the research phase, emphasizing significant data points, trends, and insights.
      - **Analytical Enhancements**: Discuss how the analysis phase added value to the initial findings, including any new insights or understandings derived from deeper examination.

    3. **Discussion**:
      - **Implications**: Explore the implications of the findings in a broader context, discussing potential impacts on the field, industry, or society.
      - **Critical Evaluation**: Critically evaluate the findings, noting strengths, weaknesses, and any contentious points that emerged during the research and analysis phases.

    4. **Recommendations**:
      - **Actionable Steps**: Provide clear, actionable recommendations based on the findings and discussions. These should be practical and tailored to specific stakeholders or policy implications.
      - **Future Research**: Suggest areas for future research that could build on the current findings, addressing any gaps or unresolved questions.

    5. **Conclusion**:
      - **Summary of Findings**: Summarize the main points of the report, reinforcing the significance and reliability of the research conducted.
      - **Final Thoughts**: Offer concluding thoughts that underscore the importance of the findings and the potential for future work in this area.

    6. **References**:
      - **Citations**: Include a detailed list of all sources cited in the document, formatted according to a recognized academic or professional standard.
      - **Source Annotations**: Optionally, provide annotations for key sources, explaining their relevance and reliability.

    7. **Appendices** (if applicable):
      - **Supporting Documents**: Attach any supporting documents, data tables, or supplementary material referenced in the report.
      - **Glossary of Terms**: Include a glossary of key terms and definitions used throughout the report for clarity.
            """
        )




