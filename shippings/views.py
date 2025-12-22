from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import ShippingAddress, ShippingMethod
from .serializers import ShippingAddressSerializer, ShippingMethodSerializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user shipping addresses.

    This ViewSet handles listing, creating, retrieving, updating, and deleting
    ShippingAddress objects. It restricts access to authenticated users only
    and ensures users can only see and manipulate their own addresses.
    """
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return the list of shipping addresses for the currently authenticated user.

        This overrides the default queryset to implement row-level security,
        ensuring users cannot access addresses belonging to others.
        """
        # Only return addresses of the logged-in user
        return ShippingAddress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the new shipping address with the currently authenticated user.

        This overrides the default create behavior to automatically associate
        the new address with the user making the request, rather than requiring
        the user ID to be passed in the request body.
        """
        serializer.save(user=self.request.user)

class ShippingMethodViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing shipping methods (e.g., Standard, Express).

    This ViewSet provides full CRUD operations for ShippingMethod objects.
    Read access is allowed for unauthenticated users (e.g., browsing the site),
    but modifications (create, update, delete) are restricted to authenticated
    users.
    """
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer

    # IsAuthenticatedOrReadOnly:
    # - Safe methods (GET, HEAD, OPTIONS) are allowed for any user (even anonymous).
    # - Unsafe methods (POST, PUT, PATCH, DELETE) require authentication.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
