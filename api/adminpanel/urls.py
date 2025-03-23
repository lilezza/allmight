from django.urls import path
from .views import UserAPI

urlpatterns = [
    path('users/',UserAPI.as_view() , name = 'users-list-create'),#create user and get all users
    path('users/<int:user_id>/',UserAPI.as_view() , name = 'manage-users'),#get specify user and update , delete user 
]
