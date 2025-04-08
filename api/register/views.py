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
            serializer.save()
            return Response({"messages":"ثبت نام با موفقیت انجام شد"} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = serializer.get_token(user)
            return Response({"messages":"ورود موفقیت امیز بود" , "tokens" : token } , status = status.HTTP_200_OK)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)