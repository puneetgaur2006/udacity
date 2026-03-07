def parse_tavily_result(tavily_response):
    results = tavily_response.get("results", [])

    if not results:
        return None

    top_result = results[0]

    return {
        "title": top_result.get("title"),
        "content": top_result.get("content"),
        "source": top_result.get("url")
    }