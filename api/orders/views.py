from django.shortcuts import render
from rest_framework import viewsets , permissions
from .models import Order , OrderItem
from .serializer import OredrSerializer , OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Order.objects.all()
    serializer_class = OredrSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer