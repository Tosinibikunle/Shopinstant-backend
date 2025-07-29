# payments/serializers.py
from .models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'reference', 'amount', 'verified', 'created_at']
        read_only_fields = ['id', 'verified', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
