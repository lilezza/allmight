from rest_framework import serializers 
from .models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['id' , 'user' , 'order' , 'amount' , 'token' , 'trans_id' , 'status' , 'request_from' , 'created_at']
        read_only_fields = ['token' , 'trans_id' , 'status' , 'created_at']