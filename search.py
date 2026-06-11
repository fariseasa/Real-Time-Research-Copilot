from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def web_search(query):
    results = client.search(
        query=query,
        max_results=5
    )

    return results

def format_results(results):

    context = ""

    for item in results["results"]:

        context += f"""
Title: {item.get('title', '')}

Content:
{item.get('content', '')}

URL:
{item.get('url', '')}

-----------------------
"""

    return context