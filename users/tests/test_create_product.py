# products/tests/test_create_product.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from products.models import Category, Product

User = get_user_model()

class CreateProductTest(APITestCase):
    def setUp(self):
       self.vendor = User.objects.create_user(
       email="vendor@example.com",
       first_name="Vend",
       last_name="Or",
       phone_number="08111112222",
       password="vendorpass123",
       is_vendor=True,    )
       
   self.token = RefreshToken.for_user(self.vendor).access_token
   self.category = Category.objects.create(name="Electronics", slug="electronics")

                                                                                                                def test_vendor_can_create_product(self):
                                                                                                                        url = reverse('product-list-create')
                                                                                                                                self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
                                                                                                                                        data = {
                                                                                                                                                    "name": "Smartphone",
                                                                                                                                                                "slug": "smartphone",
                                                                                                                                                                            "description": "Brand new smartphone",
                                                                                                                                                                                        "price": "899.99",
                                                                                                                                                                                                    "stock": 10,
                                                                                                                                                                                                                "category_id": self.category.id
                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                response = self.client.post(url, data)
                                                                                                                                                                                                                                        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                                                                                                                                                                                                                                                self.assertTrue(Product.objects.filter(name="Smartphone").exists())

                                                                                                                                                                                                                                                    def test_unauthenticated_user_cannot_create_product(self):
                                                                                                                                                                                                                                                            url = reverse('product-list-create')
                                                                                                                                                                                                                                                                    data = {
                                                                                                                                                                                                                                                                                "name": "Unauthorized Product",
                                                                                                                                                                                                                                                                                            "slug": "unauth-product",
                                                                                                                                                                                                                                                                                                        "price": "500.00",
                                                                                                                                                                                                                                                                                                                    "stock": 5,
                                                                                                                                                                                                                                                                                                                                "category_id": self.category.id
                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                response = self.client.post(url, data)
                                                                                                                                                                                                                                                                                                                                                        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)