from dotenv import load_dotenv
import os 

load_dotenv()  # Load environment variables from .env file

openai_key = os.getenv('OPENAI_API_KEY')
tavily_key = os.getenv('TAVILY_API_KEY')

print(openai_key)  # This will print your OpenAI API key
print(tavily_key)  # This will print your Tavily API key
