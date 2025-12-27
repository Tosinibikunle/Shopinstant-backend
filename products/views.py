# products/views.py
from rest_framework import generics, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


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
    PUT/PATCH/DELETE: Requires authentication.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Custom update logic.
        
        Note: This currently resets the 'seller' to the user making the request.
        If an admin edits a user's product, the admin becomes the seller.
        """
        serializer.save(seller=self.request.user)
