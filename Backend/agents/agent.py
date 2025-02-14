from langchain_core.tools import tool
from core.models import Purchase
from book.serializers import PurchaseSerializer
from rest_framework.response import Response
from rest_framework import status
import os
from core.models import Book
from book.serializers import BookSerializer
from llm import generate_response
from embeddings import main


@tool
def perform_purchase(user_id: int, book_id: int) -> dict:
    """
    Perform a purchase of a book for a user.

    Args:
        user_id (int): The ID of the user making the purchase.
        book_id (int): The ID of the book being purchased.

    Returns:
        dict: A dictionary containing the purchase details or an error message.
    """
    try:
        # Create the purchase
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

    Args:
        query (str): The search query.

    Returns:
        dict: A dictionary containing the search results or an error message.
    """
    try:

        # Perform the search
        
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