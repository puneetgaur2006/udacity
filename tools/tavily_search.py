from tavily import TavilyClient
from config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):
    response = client.search(
        query=query,
        search_depth="basic",
        max_results=3
    )
    
    return response