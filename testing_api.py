from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
API_KEY = os.getenv('OPENAI_API_KEY')

# Check if the API key was loaded
if not API_KEY:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=API_KEY)

# Create a chat completion
completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{"role":"user","text":"Hello"}],
)

# Print the response
print(completion.choices[0].message)
