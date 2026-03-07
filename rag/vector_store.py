import chromadb
import json

# Create persistent Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection WITHOUT OpenAI embedding
collection = client.get_or_create_collection(
    name="games"
)


def load_games():
    with open("data/games.json", "r") as f:
        games = json.load(f)

    for game in games:
        collection.add(
            documents=[str(game)],
            ids=[game["title"]],
            metadatas=[game]
        )

    print("Games loaded into vector database.")


def query_games(question):
    results = collection.query(
        query_texts=[question],
        n_results=1
    )
    return results

def add_web_knowledge(document_id, content, metadata):
    collection.add(
        documents=[content],
        ids=[document_id],
        metadatas=[metadata]
    )

    print("New knowledge stored in vector database.")