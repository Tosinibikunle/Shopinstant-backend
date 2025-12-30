from django.urls import path
from .views import InitializePaymentView, VerifyPaymentView

# URL Configuration for the Payments App
# This file maps the payment endpoints. Ideally included at 'api/payments/'

urlpatterns = [
    # Endpoint: /api/payments/initialize/
    # Method: POST
    # Description: Receives amount/email, calls Paystack, returns auth URL.
    path(
        "initialize/", 
        InitializePaymentView.as_view(), 
        name="initialize-payment"
    ),

    # Endpoint: /api/payments/verify/<reference_code>/
    # Method: GET
    # Description: Checks transaction status with Paystack using the unique ID.
    # The '<str:reference>' part captures the ID from the URL so it can be passed to the view.
    path(
        "verify/<str:reference>/", 
        VerifyPaymentView.as_view(), 
        name="verify-payment"
    ),
]
