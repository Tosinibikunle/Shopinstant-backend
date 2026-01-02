from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Ticket, Response, Feedback

User = get_user_model()


class TicketSerializer(serializers.ModelSerializer):
    """
    Serializer for Customer Support Tickets.
    
    This handles the creation and viewing of support requests.
    Key Logic:
    - Users can set the type, subject, and message.
    - 'is_resolved' is read-only for the user (only staff should toggle this).
    """
    
    # Display the user's string representation (e.g., email) instead of ID.
    # read_only=True because the user is set automatically by the backend.
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
        
        # Security: Prevent users from setting their own 'is_resolved' status
        # or spoofing the 'user' field or 'created_at' timestamp.
        read_only_fields = ["id", "user", "created_at", "is_resolved"]


class ResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for Staff Responses.

    Used by Customer Care Representatives to reply to tickets.
    """
    
    # Auto-populated with the logged-in staff member's details.
    customer_care_rep = serializers.StringRelatedField(read_only=True)
    
    # Link the response to a specific ticket ID.
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
    """
    Serializer for User Feedback on resolved tickets.
    """
    
    user = serializers.StringRelatedField(read_only=True)
    
    # The ticket being rated.
    # We allow null/false requirement here in case the ticket ID is passed 
    # via the URL (e.g., /api/tickets/5/feedback/) and injected by the View.
    ticket = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(), required=False, allow_null=True
    )

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
