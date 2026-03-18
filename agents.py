import os
from langchain_groq import ChatGroq
from tools import search_web

llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.environ["GROQ_API_KEY"],
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
