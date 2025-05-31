from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets , status
from .models import Tag , Brand , Categories , Attribute
from .serializer import TagSerializer , BrandSerializer , CategoriesSerializer , AttributeSerializer , CategorySimpleSerializer
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

    @action(detail=True, methods=['get'])
    def children(self, request, pk=None):
        category = self.get_object()
        children = category.children.all()
        from .serializer import CategorySimpleSerializer
        serializer = CategorySimpleSerializer(children, many=True)
        return Response({
            "id": category.id,
            "name": category.name,
            "slug": category.slug,
            "children": serializer.data
        })
    
    @action(detail = True , methods = ['get'])
    def parent(self , request , pk=None):
        category = self.get_object()
        if category.parent is None:
            return Response({'detail':'این دسته بندی والد ندارد'},status = status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(category.parent)
        return Response(serializer.data)

class AttributeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer