# orders/admin.py

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
     list_display = ('id', 'customer', 'created_at', 'is_paid', 'total_price')
     list_filter = ('is_paid', 'created_at')
     search_fields = ('customer__email',)
     inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
     list_display = ('order', 'product', 'quantity', 'price')
     search_fields = ('order__id', 'product__name')