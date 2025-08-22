# shipping/serializers.py
from .serializers import serializers
from .models import ShippingAddress, ShippingMethod


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
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
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):

        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = ["id", "name", "price", "estimated_delivery_days"]
        read_only_fields = ["id"]
