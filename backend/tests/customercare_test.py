# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from customer_care.models import CustomerCareMessage

User = get_user_model()

class CustomerCareTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="example@gmail.com",
            first_name="First",
            last_name="Last",
            phone_number="08012345678",
            password="testpass",
        )
        self.token = RefreshToken.for_user(self.user).access_token

    def test_user_can_send_message(self):
        url = reverse("customer-care")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        data = {
            "subject": "Need Help",
            "message": "I need help with my order.",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomerCareMessage.objects.count(), 1)
        self.assertEqual(CustomerCareMessage.objects.first().subject, "Need Help")



