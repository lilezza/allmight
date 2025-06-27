from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import UserAPI , UserAddressViewSet

router = DefaultRouter()
router.register(r'addresses' , UserAddressViewSet , basename= 'useraddress')

urlpatterns = [
    path('users/',UserAPI.as_view() , name = 'users-list-create'),#create user and get all users
    path('users/<int:user_id>/',UserAPI.as_view() , name = 'manage-users'),#get specify user and update , delete user 
    path('' , include(router.urls)),
]
