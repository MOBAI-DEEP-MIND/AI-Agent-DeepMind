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
