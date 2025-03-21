from django.urls import path
from .views import CreateAdminUser , ListAdminUser

urlpatterns = [
    path('create-user/', CreateAdminUser.as_view(), name='create-user'),
    path('users-list/' , ListAdminUser.as_view(), name = 'users-list' ),
]
