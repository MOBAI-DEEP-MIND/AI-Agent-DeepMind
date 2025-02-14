from core.models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView, RetrieveAPIView  ,ListAPIView  
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PurshaseSerializer,BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.models import CustomUser
from agents.agent import perform_purchase


class BookAdminView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookView(RetrieveAPIView,ListAPIView):
    """get the query of the search and return the result of the search"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



class CategoryView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]    


class AuthorView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]     


class PurchaseView(APIView):
    serializer_class = PurshaseSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = PurshaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class SearchBookView(CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

 
# class BookDetailView(RetrieveAPIView):


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
