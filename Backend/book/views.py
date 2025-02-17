from core.models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView, RetrieveAPIView  ,ListAPIView  
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PurchaseSerializer,BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.models import CustomUser
from agents.agent import perform_purchase
from agents.agent import handle_query
import random


class BookAdminListView(ListCreateAPIView):
    """Admin can list and create books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookAdminDetailView(RetrieveUpdateDestroyAPIView):
    """Admin can retrieve, update, or delete a book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookView(ListAPIView):
    """Get a list of books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Book.objects.order_by("title")[:25]  
    
class BookDetailView(RetrieveAPIView):
    """Retrieve a specific book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CategoryView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]    


class AuthorView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]     


class PurchaseView(APIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class SearchBookView(CreateAPIView):
    serializer_class = BookSearchSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        query = request.data.get("query")
        response = handle_query(query)
        print("res",response) 
        return Response({"data":response}, status=status.HTTP_200_OK)
    


 

class BookDetailView(RetrieveAPIView,ListAPIView):
    """get the query of the search and return the result of the search"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]




class PurchaseAgentView(CreateAPIView):
    """perform the purchase of the book using ai agent"""
    def post(self, request, *args, **kwargs):
        # Extract user_id and book_id from the request
        user_id = request.POST.get("user_id")
        book_id = request.POST.get("book_id")

        # Validate that user and book exist
        try:
            user = CustomUser.objects.get(id=user_id)
            book = Book.objects.get(id=book_id)
        except (CustomUser.DoesNotExist, Book.DoesNotExist):
            return Response({
                "status": "error",
                "message": "User or Book does not exist."
            }, status=status.HTTP_404_NOT_FOUND)

        # Perform the purchase using the tool
        result = perform_purchase(user_id=user_id, book_id=book_id)

        # Return the result as a JSON response
        return Response(result, status=status.HTTP_200_OK)



class PurchaseView(APIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,price=random.randint(1,100))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class BusketView(APIView):
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
    
#     def get(self,request):
#         queryset = Book.objects.all().filter(user=self.request.user)



class CreditCardView (CreateAPIView):
    """Perform a purchase of a book for a user."""
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        book_id = request.data.get("book_id")
        number_books = request.data.get("number_books")
        credit_card_number = request.data.get("credit_card_number")
        cvv = request.data.get("cvv")
        expiration_date = request.data.get("expiration_date")
        book = Book.objects.get(id=book_id)
        purchase_data = {"user": user.id, "book": book.id, "number_books": number_books, "credit_card_number": credit_card_number, "cvv": cvv, "expiration_date": expiration_date}
        serializer = PurchaseSerializer(data=purchase_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Purchase completed successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "message": "Invalid purchase data.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)