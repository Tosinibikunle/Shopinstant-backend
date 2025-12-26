# products/serializers.py
from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Product Categories.
    
    This is used both as a standalone serializer (for listing categories)
    and as a nested serializer inside ProductSerializer (to show category details).
    """
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Products.

    This serializer handles the display and creation of products.
    It uses a common pattern to handle relationships:
    1. Read operations show detailed nested objects (e.g., full category info).
    2. Write operations accept simple IDs (e.g., category ID).
    """
    
    # Read-Only Fields (for display)
    
    # Display the seller's string representation (e.g., email/username) instead of just the ID.
    seller = serializers.StringRelatedField(read_only=True)
    
    # Nest the CategorySerializer to show full details (id, name, slug) in the response.
    # read_only=True means we cannot use this field to update the category.
    category = CategorySerializer(read_only=True)

    # Write-Only Field (for input)
    
    # This field is used when creating/updating a product.
    # The client sends a Category ID (integer).
    # source="category" maps this input to the actual 'category' foreign key on the model.
    # write_only=True ensures this field doesn't appear in the API output (since we have the full 'category' object there).
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "image",
            "stock",
            "is_active",
            "category",     # Shows full object in response
            "category_id",  # Accepts ID in request
            "seller",
            "created_at",
        ]
