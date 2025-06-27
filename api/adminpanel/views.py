from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , viewsets
from .serializer import AdminUserSerializer , UserAddressSerializer
from .models import CustomUser , UserAddress
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny  # دسترسی را برای همه باز کردم
# from rest_framework.permissions import IsAdminUser

class UserAPI(APIView):
    permission_classes = [AllowAny]

    def post(self , request):
        serializer = AdminUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def get(self , request , user_id=None):
        if user_id:
            user = get_object_or_404(CustomUser , id = user_id)
            serializer = AdminUserSerializer(user)
            return Response(serializer.data , status = status.HTTP_200_OK)
        
        users = CustomUser.objects.all()
        serializer = AdminUserSerializer(users , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def put(self , request , user_id):
        user = get_object_or_404(CustomUser , id = user_id)
        serializer = AdminUserSerializer(user , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def delete(self , request , user_id):
        user = get_object_or_404(CustomUser , id = user_id)
        user.delete()
        return Response({"message":"کاربر با موفقیت حذف شد"},status = status.HTTP_204_NO_CONTENT)


class UserAddressViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer



# class UserProfileAPI(APIView):
#     permission_classes = [AllowAny]  # فعلاً دسترسی برای همه باز است

#     def get(self, request, user_id):
#         """دریافت اطلاعات یک کاربر خاص"""
#         user = get_object_or_404(CustomUser, id=user_id)
#         serializer = AdminUserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)






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
