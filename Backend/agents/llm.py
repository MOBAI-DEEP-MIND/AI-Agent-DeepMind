from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
import re

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


def clean_response(data):
    """Clean and format the LLM JSON response."""
    
    # Remove triple backticks and "json" keyword if present
    cleaned_data = re.sub(r"```json|```", "", data).strip()
    
    # Remove unnecessary newlines and extra spaces
    cleaned_data = re.sub(r"\n\s*", "", cleaned_data)
    
    # Convert to valid JSON
    try:
        books = json.loads(cleaned_data)
        return books  # Return as a list of dictionaries
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def generate_response(query, context):
    """Generate a refined query prompt based on the provided context, ensuring all book fields are included."""
    
    # Ensure context is a string
    if isinstance(context, list):
        context = "\n".join(str(item) for item in context)

    prompt = f"""
    Given the following context, identify books that satisfy the criteria of the query.

    Context:
    {context}

    Query:
    "{query}"

    Instructions:
    - Retrieve books strictly related to the query from the provided context.
    - Ensure that the response includes all relevant book fields in the following structured format:
      ```json
      [
        {{
          "Title": "(Book title)",
          "Author": "(Author's name)",
          "Publication Year": (Year of publication or null if unknown),
          "Genre": "(Book genre)",
          "Description": "(A short summary of the book)"
        }}
      ]
      ```
    - If the query is vague, infer the best possible meaning based on the context.

    Provide a **valid JSON response** that includes all book details in the expected format.
    """

    response = llm.invoke(prompt)

    # Ensure the response is a string (extracting the actual content)
    if hasattr(response, "content"):
        return clean_response(response.content)  # Extract and clean text content
    
    return {"error": "Invalid response format"}  # Fallback if response is not as expected
