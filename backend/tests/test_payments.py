
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from ...payments.models import Payment
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class PaymentTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="example@gmail.com",
            first_name="Test",
            last_name="User",
            phone_number="08012345678",
            )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        self.payment = Payment.objects.create(
            user=self.user,
            order_id=1,  # Assuming an order with ID 1 exists
            reference="REF123456",
            amount=100.00,
            status="pending",
            verified=False,
        )