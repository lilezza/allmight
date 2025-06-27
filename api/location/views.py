from rest_framework import viewsets
from .models import Province , City
from .serializer import ProvinceSerializer , CitySerializer
from rest_framework.permissions import AllowAny

class ProvinceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class cityViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = City.objects.all()
    serializer_class = CitySerializer

