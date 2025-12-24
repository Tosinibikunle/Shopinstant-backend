from django.urls import path
from .views import ShippingAddressViewSet, ShippingMethodViewSet

# URL Configuration
# This file maps URL paths to specific ViewSets and actions.
# Since we are not using a DRF 'Router' here, we manually bind HTTP methods
# (GET, POST, PUT, DELETE) to ViewSet actions (list, create, update, destroy).

urlpatterns = [
    # --- Shipping Addresses ---
    
    # Path: /api/shipping/ (assuming included at /api/shipping/)
    # Maps to the list of addresses (GET) or creating a new one (POST).
    path(
        '',
        ShippingAddressViewSet.as_view({
            'get': 'list',    # GET request -> returns a list of addresses
            'post': 'create'  # POST request -> creates a new address
        }),
        name='shipping-address-list-create'
    ),

    # Path: /api/shipping/<id>/ (e.g., /api/shipping/1/)
    # Maps to operations on a single specific address.
    path(
        '<int:pk>/',
        ShippingAddressViewSet.as_view({
            'get': 'retrieve',  # GET request -> gets one specific address
            'put': 'update',    # PUT request -> updates the address
            'delete': 'destroy' # DELETE request -> deletes the address
        }),
        name='shipping-address-detail'
    ),

    # --- Shipping Methods ---

    # Path: /api/shipping/methods/
    # Maps to the list of methods (Standard, Express, etc.) or creating a new one.
    path(
        'methods/',
        ShippingMethodViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='shipping-method-list-create'
    ),

    # Path: /api/shipping/methods/<id>/
    # Maps to operations on a single shipping method.
    path(
        'methods/<int:pk>/',
        ShippingMethodViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        }),
        name='shipping-method-detail'
    ),
]
