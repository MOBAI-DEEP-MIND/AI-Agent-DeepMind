from langchain_core.tools import tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from core.models import Purchase, Book
from book.serializers import BusketSerializer, BookSerializer
from .llm import generate_response  # Assuming this is your LLM interaction function
from .embeddings import main  # Assuming this is your embedding function


@tool
def perform_purchase(query: str, user_id: int) -> dict:
    """Perform a purchase of a book for a user."""
    try:
        books = perform_search(query)
        context_data = main(f"give me only number of books needed in this query in digits : {query}")
        res = generate_response(query, context_data)

        try:
            number_books = int(res.content)
        except ValueError:
            return {
                "status": "error",
                "message": "Invalid response from LLM: expected a number."
            }

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
def perform_search(query: str):
    """Perform a search for books based on a query."""
    try:
        context_data = main(query)
        res = generate_response(query, context_data)
        print(res.content)  # This prints the LLM's refined search query

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
        if user_id is None:
            return {
                "status": "error",
                "message": "Missing user_id for purchase."
            }
        return perform_purchase.invoke({"query": query, "user_id": user_id})



    elif tool_name == "perform_search":
        prompt_template = """Refine the following user query for a book search: {query}"""  
        prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
        llm_chain = LLMChain(llm=generate_response, prompt=prompt)  
        refined_query = llm_chain.run(query)  
        print(f"Refined Query: {refined_query}")
        return perform_search.invoke(query=refined_query)  

    else:
        return {
            "status": "error",
            "message": "Could not determine the appropriate action for your query."
        }


# # Example usage
# user_query = "I want to buy a book about AI"
# response = handle_query(user_query, user_id=1)
# print(response)

# user_query = "Find books about Python programming"
# response = handle_query(user_query)
# print(response)

# user_query = "I'm looking for a book about deep learning"
# response = handle_query(user_query)
# print(response)
