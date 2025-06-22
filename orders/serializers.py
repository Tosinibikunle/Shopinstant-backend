

from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
    queryset=ProductSerializer.Meta.model.objects.all(),
    source='product',
    write_only=True
    )

class Meta:
    model = OrderItem
    fields = ['id', 'product', 'product_id', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
  customer = serializers.StringRelatedField(read_only=True)
  items = OrderItemSerializer(many=True)

class Meta:
   model = Order
   fields = ['id', 'customer', 'created_at', 'is_paid', 'total_price', 'shipping_address', 'items']

   def create(self, validated_data):
       items_data = validated_data.pop('items')
       order = Order.objects.create(**validated_data)
       for item_data in items_data:
           OrderItem.objects.create(order=order, **item_data)
