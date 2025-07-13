# payments/serializers.py

from rest_framework import serializers
from .models import Payment
from orders.models import Order

class PaymentInitSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    email = serializers.EmailField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'reference', 'amount', 'status', 'verified', 'created_at']
        read_only_fields = ['status', 'verified', 'created_at']
