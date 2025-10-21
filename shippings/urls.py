from django.urls import path
from .views import ShippingAddressViewSet, ShippingMethodViewSet

urlpatterns = [
    path('', ShippingAddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='shipping-address-list-create'),
    path('<int:pk>/', ShippingAddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='shipping-address-detail'),

    path('methods/', ShippingMethodViewSet.as_view({'get': 'list', 'post': 'create'}), name='shipping-method-list-create'),
    path('methods/<int:pk>/', ShippingMethodViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='shipping-method-detail'),
]
