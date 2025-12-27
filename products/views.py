
from rest_framework import generics, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# --- Custom Permissions ---

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the seller of a product to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed if the user is the seller
        return obj.seller == request.user


# --- Views ---

class CategoryListView(generics.ListAPIView):
    """
    API View to list all product categories.
    
    Access: Public (AllowAny). Anyone can see the list of categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductListCreateView(generics.ListCreateAPIView):
    """
    API View to list products or create a new product.

    GET: Returns a list of all 'active' products.
    POST: Creates a new product (requires authentication).
    """
    # Only show products marked as active (e.g., in stock/not hidden)
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    
    # Authenticated users can Create (POST).
    # Unauthenticated (anonymous) users can only List (GET).
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associate the new product with the user who created it.
        """
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to retrieve, update, or delete a specific product.

    GET: Public access.
    PUT/PATCH/DELETE: Restricted to the product's seller only.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Use the custom permission class defined above.
    # This ensures User A cannot delete User B's product.
    permission_classes = [IsSellerOrReadOnly]
