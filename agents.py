import os
from langchain_groq import ChatGroq
from tools import search_web

# Read API key from environment
groq_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_key,
    temperature=0.3
)

def planner_agent(query):

    prompt = f"""
    Break the following research task into clear steps:

    {query}
    """

    return llm.invoke(prompt).content


def search_agent(query):

    results = search_web(query)

    formatted = ""

    for r in results:
        formatted += f"""
Title: {r['title']}
URL: {r['url']}
Content: {r['content']}

"""

    return formatted


def analysis_agent(data):

    prompt = f"""
    Analyze the following research data and extract key insights:

    {data}
    """

    return llm.invoke(prompt).content


def writer_agent(insights):

    prompt = f"""
    Write a detailed research report based on the following insights.

    Include:
    - Title
    - Key Insights
    - Analysis
    - Conclusion

    Insights:
    {insights}
    """

    return llm.invoke(prompt).content
