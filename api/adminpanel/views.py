from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.permissions import IsAdminUser
from .serializer import AdminUserSerializer
from rest_framework.permissions import AllowAny  # دسترسی را برای همه باز کردم

class CreateAdminUser(APIView):
    permission_classes = [AllowAny]  # فعلاً همه می‌توانند کاربر ایجاد کنند

    def post(self, request):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {
#   "username": "adminuser",
#   "first_name": "Ali",
#   "last_name": "Ahmadi",
#   "email": "admin@example.com",
#   "phone_number": "09123456789",
#   "password": "securepassword",
#   "is_staff": true,
#   "is_superuser": false
# }
