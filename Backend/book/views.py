
from core.models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PurshaseSerializer,BookSerializer

class BookView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
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