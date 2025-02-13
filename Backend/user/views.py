from rest_framework import generics
from .serializers import UserSerializer
from core.models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateUserView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class EditUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
