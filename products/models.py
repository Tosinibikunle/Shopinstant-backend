from django.db import models
from django.contrib.auth import get_user_model

# Get the active User model (handles custom user models automatically)
User = get_user_model()


class Category(models.Model):
    """
    Represents a group or type of products (e.g., 'Electronics', 'Clothing').
    Used for navigation and filtering products.
    """
    name = models.CharField(max_length=100, unique=True)
    
    # The 'slug' is a URL-friendly version of the name (e.g., "smart-phones").
    # unique=True ensures two categories don't share the same URL.
    slug = models.SlugField(unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Fixes the plural name in the Admin panel (default would be "Categorys")
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents an item listed for sale on the platform.
    """
    
    # The user who listed the product (e.g., the Vendor).
    # related_name='products' allows you to get a user's products via `user.products.all()`
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    # The category the product belongs to.
    # on_delete=models.SET_NULL: If the Category is deleted, keep the product
    # but set its category to NULL (uncategorized) rather than deleting the product.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    
    name = models.CharField(max_length=255)
    
    # URL-friendly version of the product name.
    slug = models.SlugField(unique=True)
    
    description = models.TextField(blank=True)
    
    # Always use DecimalField for money to avoid floating-point errors.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Requires Pillow library installed. Images saved to /media/products/
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    
    # Track inventory quantity.
    stock = models.PositiveIntegerField(default=0)
    
    # 'is_active' allows "soft deleting" or hiding a product without
    # actually removing it from the database (useful for order history).
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
