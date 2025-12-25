
# orders/urls.py
from django.urls import path
from .views import OrderCreateView, OrderListView

# URL Configuration for the Orders App
# This maps specific URL paths to the Class-Based Views defined in views.py.

urlpatterns = [
    # Endpoint: /api/orders/create/ (Assuming this file is included at 'api/orders/')
    # Method: POST
    # Description: Allows authenticated users to place a new order.
    path(
        "create/", 
        OrderCreateView.as_view(), 
        name="order-create"
    ),

    # Endpoint: /api/orders/my-orders/
    # Method: GET
    # Description: Returns a list of all orders belonging to the logged-in user.
    path(
        "my-orders/", 
        OrderListView.as_view(), 
        name="order-list"
    ),
]
