from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load the .env file
load_dotenv()

# Now get the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    api_key=GEMINI_API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
   
)


def generate_response (prompt,context) :
    """Generate a response from the LLM."""
    response = llm.chat(prompt, context)
    return response
