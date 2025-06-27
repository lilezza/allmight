from rest_framework import serializers
from .models import Order , OrderItem

class OredrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id' , 'user' , 'status' , 'total_amount' , 'delivery_amount' , 'paying_amount' , 'payment_status' , 'description' , 'created_at' ,
            'updated_at'
        ]
        read_only_fields = ['paying_amount' , 'created_at' , 'updated_at']

    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id' , 'order' , 'product' , 'price' , 'quantity' , 'subtotal']
        read_only_fields = ['subtotal']