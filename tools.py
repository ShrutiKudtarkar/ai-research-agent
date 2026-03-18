from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):

    results = client.search(
        query=query,
        max_results=5
    )

    return results["results"]