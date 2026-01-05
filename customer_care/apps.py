
from django.apps import AppConfig


class CustomerCareConfig(AppConfig):
    """
    Configuration class for the 'customer_care' application.

    This class provides metadata for the application and is the entry point
    for app-specific startup logic (like registering signals).
    """
    
    # Sets the default type for primary keys (IDs) for models in this app.
    # BigAutoField is a 64-bit integer, which allows for a much larger number
    # of records than the old default (AutoField).
    default_auto_field = 'django.db.models.BigAutoField'

    # The full Python path to the application (matches the folder name).
    name = 'customer_care'

    # Tip: If you use Signals (e.g., to notify a user when a ticket is updated),
    # you should override the ready() method to import them here.
    # 
    # def ready(self):
    #     import customer_care.signals
