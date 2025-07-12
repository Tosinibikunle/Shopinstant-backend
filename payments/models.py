# payments/models.py

from django.db import models
from django.utils import timezone
from orders.models import Order

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
                 ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    reference = models.CharField(max_length=100, unique=True)
                                            amount = models.DecimalField(max_digits=10, decimal_places=2)
                                                status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
                                                    created_at = models.DateTimeField(default=timezone.now)
                                                        verified = models.BooleanField(default=False)

                                                            def __str__(self):
                                                                    return f"Payment for Order #{self.order.id} - {self.status}"

