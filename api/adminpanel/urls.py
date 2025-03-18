from django.urls import path
from .views import CreateAdminUser

urlpatterns = [
    path('create-admin/', CreateAdminUser.as_view(), name='create-admin'),
]
