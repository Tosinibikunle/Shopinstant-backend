

# Create your views here
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import ShippingAddress, ShippingMethod
from .serializers import ShippingAddressSerializer, ShippingMethodSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return addresses of the logged-in user
        return ShippingAddress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShippingMethodViewSet(viewsets.ModelViewSet):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
