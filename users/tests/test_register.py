# users/tests/test_register.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserTest(APITestCase):
   def test_user_can_register_successfully(self):
      url = reverse('register')
      data = {
          "email": "test@example.com",
          "first_name": "Test",
          "last_name": "User",
          "phone_number": "08012345678",
          "password": "securepass123",
          "password2": "securepass123"
          }
      response = self.client.post(url, data)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertTrue(User.objects.filter(email="test@example.com").exists())
      self.assertIn("token", response.data)