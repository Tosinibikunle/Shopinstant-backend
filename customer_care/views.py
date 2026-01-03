
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Ticket, Response, Feedback
from .serializers import TicketSerializer, ResponseSerializer, FeedbackSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Support Tickets.

    Allows users to create new tickets and view their status.
    """
    # WARNING: This currently allows ANY logged-in user to see ALL tickets.
    # You should override get_queryset() to filter by user (see below).
    queryset = Ticket.objects.all()
    
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optional: Override to ensure users only see their own tickets.
        """
        user = self.request.user
        # If user is staff/admin, show all tickets.
        if user.is_staff:
            return Ticket.objects.all()
        # Otherwise, only show tickets belonging to the logged-in user.
        return Ticket.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Link the new ticket to the currently logged-in user.
        """
        serializer.save(user=self.request.user)


class ResponseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Staff Responses.

    This allows Customer Care Reps to post replies to tickets.
    """
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    
    # Ideally, only Staff should be able to create responses.
    # You might want to change this to: [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Link the response to the staff member creating it.
        """
        serializer.save(customer_care_rep=self.request.user)


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User Feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Link the feedback to the user submitting it.
        """
        serializer.save(user=self.request.user)
