from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Ticket(models.Model):
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
        return f"{self.ticket_type.title()} from {self.user.email} - {self.subject}"

    class Meta:
        verbose_name_plural = "Tickets"
        ordering = ["-created_at"]


class Response(models.Model):
    customer_care_rep = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="given_responses"
    )
    # Generic relation to Ticket
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="responses")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.customer_care_rep.email} on {self.ticket}"


class Feedback(models.Model):
    ticket = models.OneToOneField(
        Ticket, on_delete=models.CASCADE, related_name="feedback", null=True, blank=True
    )  # feedback tied to a resolved ticket
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    message = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField()  # out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.email} - Rating: {self.rating}"

    class Meta:
        verbose_name_plural = "Feedbacks"
