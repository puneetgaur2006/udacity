from rag.vector_store import load_games, query_games
from agent.response_formatter import format_game_response
from agent.evaluator import evaluate_confidence


def main():
    load_games()

    question = input("Ask about a game: ")
    results = query_games(question)


    top_document = results["documents"][0][0]
    distance = results["distances"][0][0]
    confidence = evaluate_confidence(distance)
    print("Distance:", distance)
    print(confidence)
    formatted_response = format_game_response(
    top_document,
    source="Local Dataset",
    confidence=confidence
)

    #print(formatted_response)


if __name__ == "__main__":
    main()