
from django.apps import AppConfig


class CustomerCareConfig(AppConfig):
    """
    Configuration class for the 'customer_care' application.

    This class provides metadata for the application and is the entry point
    for app-specific startup logic (like registering signals).
    """
    
    default_auto_field = 'django.db.models.BigAutoField'

    name = 'customer_care'
