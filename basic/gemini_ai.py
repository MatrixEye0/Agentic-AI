import os
from dotenv import load_dotenv
from google import genai

load_dotenv("basic/.env") #load .env
api_key = os.getenv("GEMINI_API_KEY")# get api key

client = genai.Client(api_key=api_key) # create gemini client

generation_config = {
    'max_output_tokens': 1000,
    'thinking_level': 'medium',
}

# Send request
response = client.interactions.create(
    model = "gemini-flash-latest",
    input = "Roadmap for  AI coding assistant ",
    generation_config=generation_config,
)

# response 
print("==== GEMINI ====")
print(response.output_text)