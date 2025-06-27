from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProvinceViewSet , cityViewSet

router = DefaultRouter()
router.register(r'province',ProvinceViewSet)
router.register(r'cities' , cityViewSet)

urlpatterns = [
    path('' , include(router.urls)),
]