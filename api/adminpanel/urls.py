from django.urls import path
from .views import CreateAdminUser , ListAdminUser

urlpatterns = [
    path('create-admin/', CreateAdminUser.as_view(), name='create-admin'),
    path('list-users/' , ListAdminUser.as_view(), name = 'list-users' ),
]
