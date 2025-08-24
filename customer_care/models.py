from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Enguiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enquiries")
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)


    def __str__(self):
        return f"Enquiry from {self.user.email} - {self.subject}"  
    class Meta:
        verbose_name_plural = "Enquiries"   

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Complaint from {self.user.email} - {self.subject}"
    
    class Meta:
        verbose_name_plural = "Complaints"       

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    message = models.TextField()
    rating = models.PositiveIntegerField()  # Assuming a rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.email} - Rating: {self.rating}"
    
    class Meta:
        verbose_name_plural = "Feedbacks"

class Response(models.Model):
    customer_care_rep = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    enquiry = models.ForeignKey(Enguiry, on_delete=models.CASCADE, related_name="responses", null=True, blank=True)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name="responses", null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.customer_care_rep.email}"
    
    class Meta:
        verbose_name_plural = "Responses"                