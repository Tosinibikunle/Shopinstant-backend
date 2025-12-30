from django.contrib import admin
from .models import Payment


@admin.register(Payment)


class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ("order", "reference", "amount", "status", "verified", "created_at")
    list_filter = ("status", "verified", "created_at")
    search_fields = ("reference", "order__id")
