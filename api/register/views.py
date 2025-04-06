from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from adminpanel.models import CustomUser
from .serializer import RegisterSerializer , LoginSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user" : RegisterSerializer(user).data ,
                "refresh" : str(refresh),
                "access" : str(refresh.access_token)
            })
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = serializer.get_token(user)
            return Response(token , status = status.HTTP_200_OK)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)