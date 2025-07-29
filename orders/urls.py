# orders/urls.py

from django.urls import path
from .views import OrderCreateView, OrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('my-orders/', OrderListView.as_view(), name='order-list'),
]
