from django.urls import path
from .views import ShippingAddressViewSet, ShippingMethodViewSet


urlpatterns = [
    
        ShippingAddressViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='shipping-address-list-create'
    ),

    path(
        '<int:pk>/',
        ShippingAddressViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
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
