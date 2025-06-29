# cart/views.py

from rest_framework import generics, permissions
from .models import CartItem
from .serializers import CartItemSerializer

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self)
       return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
       existing_item = CartItem.objects.filter(user=self.request.user,product=serializer.validated_data['product] ).first()

      if existing_item:
         existing_item.quantity += serializer.validated_data.get('quantity', 1)
         existing_item.save()
      else:
        serializer.save(user=self.request.user)

class CartItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = CartItemSerializer
     permission_classes = [permissions.IsAuthenticated]

     def get_queryset(self):
                     return CartItem.objects.filter(user=self.request.user)