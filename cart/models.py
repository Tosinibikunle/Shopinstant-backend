# cart/models.py

from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class CartItem(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)
          added_at = models.DateTimeField(auto_now_add=True)

                    class Meta:
                            unique_together = ['user', 'product']

                                def __str__(self):
                                        return f"{self.quantity} x {self.product.name} in {self.user.email}'s cart"