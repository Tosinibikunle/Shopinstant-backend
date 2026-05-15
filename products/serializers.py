
from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductSerializer(serializers.ModelSerializer):
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
