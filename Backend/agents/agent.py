from langchain_core.tools import tool
from core.models import Purchase, Book
from book.serializers import PurchaseSerializer, BookSerializer
from llm import generate_response
from embeddings import main

@tool
def perform_purchase(user_id: int, book_id: int) -> dict:
    """
    Perform a purchase of a book for a user.
    """
    try:
        purchase_data = {"user": user_id, "book": book_id}
        serializer = PurchaseSerializer(data=purchase_data)
        
        if serializer.is_valid():
            serializer.save()
            return {
                "status": "success",
                "message": "Purchase completed successfully.",
                "data": serializer.data
            }
        else:
            return {
                "status": "error",
                "message": "Invalid purchase data.",
                "errors": serializer.errors
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@tool
def perform_search(query: str) -> dict:
    """
    Perform a search for books based on a query.
    """
    try:
        context_data = main(query)
        res = generate_response(query, context_data)
        print(res.content)

        books = Book.objects.filter(title__icontains=res.content)
        serializer = BookSerializer(books, many=True)
        return serializer.data
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def determine_tool(query: str) -> str:
    """
    Determine which tool to use based on the user's query.
    """
    # Define keywords for each tool
    purchase_keywords = ["buy", "purchase", "order", "get book"]
    search_keywords = ["search", "find", "look for", "book about"]

    # Check for keywords in the query
    if any(keyword in query.lower() for keyword in purchase_keywords):
        return "perform_purchase"
    elif any(keyword in query.lower() for keyword in search_keywords):
        return "perform_search"
    else:
        return None

def handle_query(query: str, **kwargs) -> dict:
    """
    Handle the user query by routing it to the appropriate tool.
    """
    tool_name = determine_tool(query)
    
    if tool_name == "perform_purchase":
        # Extract user_id and book_id from kwargs or query
        user_id = kwargs.get("user_id")
        book_id = kwargs.get("book_id")
        if user_id is None or book_id is None:
            return {
                "status": "error",
                "message": "Missing user_id or book_id for purchase."
            }
        return perform_purchase(user_id, book_id)
    
    elif tool_name == "perform_search":
        return perform_search(query)
    
    else:
        return {
            "status": "error",
            "message": "Could not determine the appropriate action for your query."
        }

# Example usage
user_query = "I want to buy book with ID 123"
response = handle_query(user_query, user_id=1, book_id=123)
print(response)

user_query = "Find books about Python programming"
response = handle_query(user_query)
print(response)