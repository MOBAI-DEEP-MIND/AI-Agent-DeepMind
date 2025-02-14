from langchain_core.tools import tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from core.models import Purchase, Book
from book.serializers import BusketSerializer, BookSerializer
from llm import generate_response  # Assuming this is your LLM interaction function
from embeddings import main  # Assuming this is your embedding function


@tool
def perform_purchase(query,user_id) -> dict:
    """Perform a purchase of a book for a user."""
    try:

        books = perform_search(query)
        context_data = main("give me only number of books needed in this query in digits : {query}")
        res = generate_response(query, context_data)
        number_books = int(res.content)
        books = perform_search(query)
        books = books[:number_books]
        busket = {
            "user": user_id,
            "book": books
        }
        serializer = BusketSerializer(data=busket)
        if serializer.is_valid():
            serializer.save()
            return {
                "status": "success",
                "message": "Book added to busket."
            }
        else:
            return {
                "status": "error",
                "message": serializer.errors
            }
      
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@tool
def perform_search(query: str) :
    """Perform a search for books based on a query."""
    try:
        context_data = main(query)
        res = generate_response(query, context_data)
        print(res.content) # This prints the LLM's refined search query

        books = Book.objects.filter(title__icontains=res.content)  # Use LLM output for filtering
        serializer = BookSerializer(books, many=True)
        return serializer.data
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


def determine_tool(query: str) -> str:
    """Determine which tool to use based on the user's query."""
    purchase_keywords = ["buy", "purchase", "order", "get book"]
    search_keywords = ["search", "find", "look for", "book about"]

    if any(keyword in query.lower() for keyword in purchase_keywords):
        return "perform_purchase"
    elif any(keyword in query.lower() for keyword in search_keywords):
        return "perform_search"
    else:
        return None



def handle_query(query: str, **kwargs) -> dict:
    """Handle the user query using Langchain chains."""

    tool_name = determine_tool(query)

    if tool_name == "perform_purchase":
        user_id = kwargs.get("user_id")
        book_id = kwargs.get("book_id")
        if user_id is None or book_id is None:
            return {
                "status": "error",
                "message": "Missing user_id or book_id for purchase."
            }
        return perform_purchase(user_id, book_id)

    elif tool_name == "perform_search":
        # Langchain Prompt and Chain for refining the search query (Optional but recommended)
        prompt_template = """Refine the following user query for a book search: {query}""" # Improve prompt
        prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
        # Assuming generate_response is compatible with Langchain
        llm_chain = LLMChain(llm=generate_response, prompt=prompt) # You might need to adapt this
        refined_query = llm_chain.run(query) # Run the chain
        print(f"Refined Query: {refined_query}")
        return perform_search(refined_query)  # Use the refined query

    else:
        return {
            "status": "error",
            "message": "Could not determine the appropriate action for your query."
        }



# Example usage (same as before)
user_query = "I want to buy book with ID 123"
response = handle_query(user_query, user_id=1, book_id=123)
print(response)

user_query = "Find books about Python programming"
response = handle_query(user_query)
print(response)

user_query = "I'm looking for a book about deep learning" # Test with more complex query
response = handle_query(user_query)
print(response)