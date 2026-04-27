from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ticket(models.Model):
    """
    Represents a customer support issue or inquiry.
    
    This is the central model for the support system. Users create tickets,
    and customer care reps respond to them.
    """
    
    ENQUIRY = "enquiry"
    COMPLAINT = "complaint"
    REQUEST = "request"

    TICKET_TYPES = [
        (ENQUIRY, "Enquiry"),
        (COMPLAINT, "Complaint"),
        (REQUEST, "Request"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        """String representation: 'Complaint from user@example.com - Login Issue'"""
        return f"{self.ticket_type.title()} from {self.user} - {self.subject}"

    class Meta:
        verbose_name_plural = "Tickets"
        ordering = ["-created_at"]


class Response(models.Model):
    """
    Represents a reply to a Ticket, typically from a Customer Care Representative.
    """

    customer_care_rep = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="given_responses"
    )
    
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="responses"
    )
    
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.customer_care_rep} on {self.ticket}"


class Feedback(models.Model):
    """
    User feedback regarding a specific Ticket resolution.
    """
    
    ticket = models.OneToOneField(
        Ticket, on_delete=models.CASCADE, related_name="feedback", null=True, blank=True
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    
    message = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user} - Rating: {self.rating}"

    class Meta:
        
        verbose_name_plural = "Feedbacks"
