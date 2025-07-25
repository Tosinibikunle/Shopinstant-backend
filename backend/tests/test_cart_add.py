# cart/tests/test_cart_add.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from products.models import Category, Product
from cart.models import CartItem

User = get_user_model()


class AddToCartTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="cartuser@example.com",
            first_name="Cart",
            last_name="User",
            phone_number="08000000000",
            password="testcart123"
        )

        self.token = RefreshToken.for_user(self.user).access_token
        self.category = Category.objects.create(name="Books", slug="books")
        self.product = Product.objects.create(
            name="Django for APIs", slug="django-apis", price=49.99,  stock=5, seller=self.user,  category=self.category)

    def test_add_product_to_cart(self):
        url = reverse('cart-list-create')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        data = {
            "product_id": self.product.id,
            "quantity": 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CartItem.objects.filter(
            user=self.user, product=self.product).exists())

    def test_unauthenticated_user_cannot_add_to_cart(self):
        url = reverse('cart-list-create')
        data = {
            "product_id": self.product.id,
            "quantity": 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
