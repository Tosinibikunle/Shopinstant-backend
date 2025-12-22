from rest_framework import serializers
from .models import ShippingAddress, ShippingMethod


class ShippingAddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShippingAddress model.

    This handles the conversion of ShippingAddress instances to JSON and vice-versa.
    It includes a custom 'create' method to automatically associate the new address
    with the currently authenticated user.
    """
    class Meta:
        model = ShippingAddress
        # List of fields to be included in the API response/request
        fields = [
            "id",
            "full_name",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "postal_code",
            "country",
            "phone_number",
            "is_default",
            "created_at",
        ]
        # Fields that can be seen in the response but cannot be modified by the user
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        """
        Override the default create method to attach the current user.

        This ensures that when a new address is created, it is automatically
        linked to the user making the request (retrieved from the serializer context),
        rather than requiring the user to submit their own ID.
        """
        # Retrieve the user from the request context passed by the ViewSet
        user = self.context["request"].user
        
        # Add the user to the validated data before saving
        validated_data["user"] = user
        
        return super().create(validated_data)


class ShippingMethodSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShippingMethod model.

    This is a standard serializer used to display available shipping options
    (e.g., name, price, delivery time) to the frontend.
    """
    class Meta:
        model = ShippingMethod
        fields = ["id", "name", "price", "estimated_delivery_days"]
        read_only_fields = ["id"]
