# users/tests/test_login.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginUserTest(APITestCase):
   def setUp(self):
      self.user = User.objects.create_user(
      email="login@example.com",
      first_name="Login",
      last_name="Tester",
      phone_number="08099998888",
      password="testpass123"
        )

   def test_user_can_login_with_valid_credentials(self):
      url = reverse('login')
      data = {
         "email": "login@example.com",
         "password": "testpass123"
                     }
      response = self.client.post(url, data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn("token", response.data)
      self.assertIn("access", response.data["token"])
      self.assertIn("refresh", response.data["token"])