# products/admin.py

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Product)
            class ProductAdmin(admin.ModelAdmin):
                list_display = ('name', 'slug', 'seller', 'price', 'stock', 'is_active', 'created_at')
                    list_filter = ('is_active', 'category')
                        search_fields = ['name', 'description']
                            prepopulated_fields = {'slug': ('name',)}