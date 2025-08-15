from django.contrib import admin

from .models import ShippingAddress, ShippingMethod  

# Register your models here.
@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "full_name",
        "city",
        "state",
        "postal_code",
        "country",
        "is_default",
        "created_at",
    )
    search_fields = ("user__email", "full_name", "city", "state", "postal_code")
    list_filter = ("is_default", "country", "created_at")