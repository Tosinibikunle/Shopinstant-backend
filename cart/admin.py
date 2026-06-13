
from django.contrib import admin
from .models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user','user_id', 'product', 'quantity', 'added_at')
    search_fields = ('user__email', 'product__name', 'product_id')
    list_filter = ('added_at',)
