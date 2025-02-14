from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from embeddings import main

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

def generate_response(query, context):
    """Generate a refined query prompt based on the provided context."""
    
    # Ensure context is a string (if it's a list, join elements)
    if isinstance(context, list):
        context = "\n".join(str(item) for item in context)

    prompt = f"""
    Given the following context, formulate a well-structured response to the query.

    Context:
    {context}

    Query:
    give me book titles that satisify the criteria of query
    "{query}"

    Instructions:
    - Retrieve information strictly related to the query from the provided context.
    - Ensure the response is clear, concise, and relevant.
    - If the query is vague, infer the best possible meaning based on the context.

    Provide the best response based on the available context.
    """
    

    response = llm.invoke(prompt)
    return response


