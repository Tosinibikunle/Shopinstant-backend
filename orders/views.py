from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    """
    API View to create a new Order.

    This view handles POST requests to create a new order. It ensures that
    only authenticated users can create orders and automatically associates
    the new order with the logged-in user.
    """
    serializer_class = OrderSerializer
    
    # Require the user to be logged in to access this endpoint.
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom logic during the creation process.

        We override this method to inject the currently logged-in user
        as the 'customer' of the order. This prevents the user from
        having to manually submit their own user ID (or spoofing someone else's).
        """
        # Save the order with the user from the request object
        serializer.save(customer=self.request.user)


class OrderListView(generics.ListAPIView):
    """
    API View to list all Orders for the current user.

    This view handles GET requests. It filters the database to return
    only the orders that belong to the user making the request.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return the list of items for this view.

        This overrides the default behavior (which would return all orders)
        to implement Row-Level Security.
        """
        # Filter orders so the user only sees their own history
        return Order.objects.filter(customer=self.request.user)
