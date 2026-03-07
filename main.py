from rag.vector_store import load_games, query_games, add_web_knowledge
from agent.response_formatter import format_game_response
from agent.evaluator import evaluate_confidence
from tools.tavily_search import search_web
from agent.web_parser import parse_tavily_result


def main():
    # Load initial dataset
    load_games()

    question = input("Ask about a game: ")

    # Query vector database
    results = query_games(question)

    top_document = results["documents"][0][0]
    distance = results["distances"][0][0]

    print("Distance:", distance)

    # Evaluate confidence
    confidence = evaluate_confidence(distance)

    # If confidence is low → search web
    if confidence == "Low":
        print("\n⚠ Low confidence. Searching web...\n")

        web_result = search_web(question)

        parsed = parse_tavily_result(web_result)

        if parsed is None:
            print("No useful web results found.")
            return

        print("\n🌐 Web Result Found\n")
        print("Title:", parsed["title"])
        print("Content:", parsed["content"])
        print("Source:", parsed["source"])

        # Persist knowledge in vector database
        add_web_knowledge(
        document_id=parsed["title"],
        content=parsed["content"],
        metadata={"source": parsed["source"], "type": "web"}
    )
        print("\n📚 Learned new knowledge from the web.")

        print("\nAnswer:")
        print(parsed["content"])

        return

    # If confidence is good → answer from local dataset
    formatted_response = format_game_response(
        top_document,
        source="Local Dataset",
        confidence=confidence
    )

    print(formatted_response)


if __name__ == "__main__":
    main()