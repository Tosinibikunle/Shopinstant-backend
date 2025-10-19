

from django.urls import path
from django.shortcuts import render
from .views import CartItemListCreateView, CartItemUpdateDeleteView

urlpatterns = [
    path('', CartItemListCreateView.as_view(), name='cart-list-create'),
    path('<int:pk>/', CartItemUpdateDeleteView.as_view(), name='cart-update-delete'),
    path('', lambda request: render(request, './templates/home.html')),  # Updated line to render home.html
        ]