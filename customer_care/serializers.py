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


class ResponseSerializer(serializers.ModelSerializer):
    customer_care_rep = serializers.StringRelatedField(read_only=True)
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())

    class Meta:
        model = Response
        fields = [
            "id",
            "customer_care_rep",
            "ticket",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "customer_care_rep", "created_at"]        
class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Feedback
        fields = [
            "id",
            "ticket",
            "user",
            "message",
            "rating",
            "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]