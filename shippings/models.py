
from django.db import models
from django.contrib.auth import get_user_model

# Get the active User model for the project.
# This is a best practice in Django: it ensures your code works even if
# you have swapped out the default User model for a custom one.
User = get_user_model()


class ShippingAddress(models.Model):
    """
    Represents a physical delivery location for a user.

    A user can have multiple shipping addresses, but typically only one
    will be marked as the default.
    """
    
    # Relationship to the User model.
    # on_delete=models.CASCADE: If the User is deleted, delete all their addresses too.
    # related_name='shipping_addresses': Allows accessing addresses like `user.shipping_addresses.all()`
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shipping_addresses'
    )
    
    full_name = models.CharField(max_length=255)  # Name of the person receiving the package
    address_line1 = models.CharField(max_length=255)  # Street address, P.O. Box
    
    # Optional field for apartment, suite, unit, etc.
    # blank=True allows the form to be empty; null=True allows the DB to store NULL.
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)  # Contact for delivery driver
    
    # Flag to indicate if this is the user's primary address.
    # Logic to ensure only one is True per user should be handled in the view/serializer.
    is_default = models.BooleanField(default=False)
    
    # Automatically set the timestamp when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation: e.g., 'John Doe - New York'"""
        return f"{self.full_name} - {self.city}"


class ShippingMethod(models.Model):
    """
    Represents the available shipping options (e.g., Standard, Express, Next-Day).
    These are usually set up by the site admin, not the end user.
    """
    name = models.CharField(max_length=100)
    
    # Use DecimalField for currency to avoid floating-point rounding errors.
    # max_digits=10, decimal_places=2 allows values up to 99,999,999.99
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Integer field for the estimated time (e.g., 3 days, 5 days).
    estimated_delivery_days = models.PositiveIntegerField()

    def __str__(self):
        """String representation: e.g., 'Express Delivery ($15.00)'"""
        return f"{self.name} (${self.price})"
