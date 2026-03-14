# UdaPlay Agent - RAG Solution Project

A Retrieval-Augmented Generation (RAG) agent that combines vector database retrieval with web search to answer questions about video games.

## Overview

This notebook implements a **hybrid Q&A system** that:
1. First tries to answer questions using internal knowledge stored in a vector database
2. Uses an LLM to evaluate if the retrieved information is relevant
3. Falls back to web search (Tavily) when internal knowledge is insufficient

## Architecture

```
┌─────────────┐     ┌──────────┐     ┌────────────┐
│   RETRIEVE  │────>│ EVALUATE │────>│   ANSWER   │
└─────────────┘     └──────────┘     └────────────┘
       │                   │                 │
       │                   │                 │
       │                   v                 │
       │             ┌──────────┐             │
       └───────────>│WEB_SEARCH │─────────────┘
                    └──────────┘
```

### Components

| Component | Description |
|-----------|-------------|
| **ChromaDB** | Vector database storing game metadata with sentence embeddings (all-MiniLM-L6-v2) |
| **retrieve_game_tool()** | Queries the vector database for relevant game information |
| **evaluate_retrieval_tool()** | Uses Ollama Mistral to validate if retrieved docs answer the question |
| **web_search_tool()** | Tavily API integration for external web search |
| **UdaPlayAgent** | Main agent class implementing the state machine |

## Dependencies

- `chromadb` - Vector database
- `chromadb.utils.embedding_functions` - Sentence transformer embeddings
- `ollama` - Local LLM (Mistral model)
- `tavily` - Web search API
- `json` - Data parsing
- `uuid` - Unique ID generation

## Key Functions

### retrieve_game_tool(query)
Queries the ChromaDB collection for game information using semantic search.

### evaluate_retrieval_tool(question, document)
Uses Mistral LLM to determine if the retrieved document is useful for answering the question.

### web_search_tool(query)
Performs web search using Tavily API as a fallback for unknown queries.

### UdaPlayAgent
Main agent class with state machine logic:
- **RETRIEVE**: Query vector database
- **EVALUATE**: Check relevance with LLM
- **ANSWER**: Return formatted response
- **WEB_SEARCH**: Search web if internal knowledge fails

## Usage Examples

```python
# Create agent instance
agent = UdaPlayAgent()

# Ask questions about games
agent.run("Who developed FIFA 21?")
agent.run("When was Tekken 7 released?")
agent.run("When is GTA 6 released?")
```

## Test Cases

The notebook demonstrates several scenarios:

| Query | Result |
|-------|--------|
| "Who developed FIFA 21?" | ✅ Answered from internal knowledge |
| "When was Tekken 7 released?" | ✅ Answered from internal knowledge |
| "When is GTA 6 released?" | 🔄 Fallback to web search (not in database) |
| "When was Cricket 19 released and who was the publisher?" | 🔄 Fallback to web search |

## Environment Variables

- `TAVILY_API_KEY` - API key for Tavily web search
- `OPENAI_API_KEY` - (Optional) For OpenAI GPT models (currently using Ollama instead)

## Data Source

Game data is loaded from JSON files in the `games/` directory:
- `fifa21.json`
- `gow_ragnarok.json`
- `pubg.json`
- `road_rash.json`
- `tekken7.json`

## Notes

- The agent treats "developer" and "publisher" as synonymous concepts
- Follow-up questions like "When was it?" are resolved using conversation history
- Web search results are not currently stored back to the vector database (commented out)
