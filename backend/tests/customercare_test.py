# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from customer_care.models import Response, Ticket, Feedback
from django.db import models

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
        self.assertEqual(Response.objects.count(), 1)
        self.assertEqual(Response.objects.first().subject, "Need Help")
        self.assertEqual(Response.objects.first().message, "I need help with my order.")

    def test_unauthenticated_user_cannot_send_message(self):
        url = reverse("customer-care")
        data = {
            "subject": "Need Help",
            "message": "I need help with my order.",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Response.objects.count(), 0)

    def test_user_cannot_send_message_with_invalid_data(self):
        url = reverse("customer-care")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        data = {
            "subject": "",
            "message": "",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Response.objects.count(), 0)

    def test_user_can_retrieve_their_messages(self):
        Response.objects.create(
            user=self.user,
            subject="First Message",
            message="This is the first message."
        )
        Response.objects.create(
            user=self.user,
            subject="Second Message",
            message="This is the second message."
        )
        url = reverse("customer-care")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)            
