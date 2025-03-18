from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AdminUserSerializer
from rest_framework.permissions import IsAdminUser

class CreateAdminUser(APIView):
    permission_classes = [IsAdminUser]  # فقط ادمین‌ها اجازه دارن

    def post(self, request):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            admin_user = serializer.save()
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
