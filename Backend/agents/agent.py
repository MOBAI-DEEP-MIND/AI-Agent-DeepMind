from langchain_core.tools import tool
from core.models import Purchase
from book.serializers import PurchaseSerializer
from rest_framework.response import Response
from rest_framework import status
import os
# from langchain import Langchain




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