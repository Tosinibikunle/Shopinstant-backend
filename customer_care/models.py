from django.db import models
from django.contrib.auth import get_user_model

# We use get_user_model() to support custom User models (e.g., if you use email instead of username)
User = get_user_model()


class Ticket(models.Model):
    """
    Represents a customer support issue or inquiry.
    
    This is the central model for the support system. Users create tickets,
    and customer care reps respond to them.
    """
    
    # Constants for ticket types to avoid "magic strings" in the code.
    ENQUIRY = "enquiry"
    COMPLAINT = "complaint"
    REQUEST = "request"

    TICKET_TYPES = [
        (ENQUIRY, "Enquiry"),
        (COMPLAINT, "Complaint"),
        (REQUEST, "Request"),
    ]

    # The user who opened the ticket.
    # related_name="tickets" allows accessing a user's tickets via `user.tickets.all()`
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    # Auto-set the timestamp when created.
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Status flag. You might want to expand this to choices (Open, In Progress, Resolved) later.
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        """String representation: 'Complaint from user@example.com - Login Issue'"""
        return f"{self.ticket_type.title()} from {self.user} - {self.subject}"

    class Meta:
        verbose_name_plural = "Tickets"
        # Default ordering: Newest tickets first
        ordering = ["-created_at"]


class Response(models.Model):
    """
    Represents a reply to a Ticket, typically from a Customer Care Representative.
    """
    
    # The staff member who is replying.
    customer_care_rep = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="given_responses"
    )
    
    # The ticket this response belongs to.
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
    
    # OneToOneField ensures only ONE feedback entry per ticket.
    # null=True, blank=True allows the ticket to exist without feedback initially.
    ticket = models.OneToOneField(
        Ticket, on_delete=models.CASCADE, related_name="feedback", null=True, blank=True
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    
    # Optional comment from the user.
    message = models.TextField(blank=True, null=True)
    
    # Rating (e.g., 1-5 stars). 
    # You might want to add validation here later (e.g., validators=[MinValueValidator(1), MaxValueValidator(5)])
    rating = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user} - Rating: {self.rating}"

    class Meta:
        # Note: "Feedback" is technically uncountable in English, but "Feedbacks" is common in database naming.
        verbose_name_plural = "Feedbacks"
