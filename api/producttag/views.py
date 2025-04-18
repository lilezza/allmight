from rest_framework import viewsets
from .models import Tag
from .serializer import TagSerializer
from rest_framework.permissions import AllowAny

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer