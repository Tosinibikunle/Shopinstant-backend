
from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Payment model.

    This handles the recording of payment attempts in the database.
    Note: 'verified' is read-only to prevent users from manually marking
    their own payments as successful via the API.
    """
    class Meta:
        model = Payment
        fields = ["id", "reference", "amount", "verified", "created_at"]
        
        # Security: These fields cannot be set by the user during creation.
        # - verified: Only the backend (via Paystack webhook/verification) handles this.
        # - created_at: Automatically set by the database.
        read_only_fields = ["id", "verified", "created_at"]

    def create(self, validated_data):
        """
        Override create to associate the payment with the logged-in user.
        """
        # Get the user from the request context (passed by the View/ViewSet)
        user = self.context["request"].user
        
        # Add the user to the data before saving
        validated_data["user"] = user
        
        return super().create(validated_data)
