from models import Ticket, Response, Feedback
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class TicketSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            "id",
            "user",
            "ticket_type",
            "subject",
            "message",
            "created_at",
            "is_resolved",
        ]
        read_only_fields = ["id", "user", "created_at", "is_resolved"]
