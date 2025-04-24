from rest_framework import viewsets
from .models import Tag , Brand , Categories , Attribute
from .serializer import TagSerializer , BrandSerializer , CategoriesSerializer , AttributeSerializer
from rest_framework.permissions import AllowAny

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class AttributeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer