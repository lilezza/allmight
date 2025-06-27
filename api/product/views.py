from rest_framework import viewsets
from .models import Product , ProductImage
from .serializer import ProductSerializer , ProductImageSerializer
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer