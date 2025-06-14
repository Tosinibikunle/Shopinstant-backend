# products/views.py

from rest_framework import generics, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
        serializer_class = CategorySerializer
            permission_classes = [permissions.AllowAny]

            class ProductListCreateView(generics.ListCreateAPIView):
                queryset = Product.objects.filter(is_active=True)
                    serializer_class = ProductSerializer
                        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

                            def perform_create(self, serializer):
                                    serializer.save(seller=self.request.user)

                                    class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
                                        queryset = Product.objects.all()
                                            serializer_class = ProductSerializer
                                                permission_classes = [permissions.IsAuthenticatedOrReadOnly]

                                                    def perform_update(self, serializer):
                                                            serializer.save(seller=self.request.user)