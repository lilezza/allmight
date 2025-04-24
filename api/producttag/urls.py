from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet , BrandViewSet , CategoriesViewSet ,AttributeViewSet

router = DefaultRouter()
router.register('tags' , TagViewSet , basename = 'tag')
router.register(r'brands' , BrandViewSet , basename = 'brand')
router.register(r'categories' , CategoriesViewSet , basename = 'category')
router.register(r'attributes' , AttributeViewSet , basename = 'attribute')

urlpatterns = [
    path('' , include(router.urls)),
]