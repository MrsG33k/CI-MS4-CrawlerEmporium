from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SupportTicket(models.Model):
    # Severity status choices matching system lore
    SEVERITY_CHOICES = [
        ('low', 'Low - Minor Inconvenience'),
        ('medium', 'Medium - Some feathers are fuffled here.'),
        ('high', 'High - This is seriously a problem'),
        ('critical', ' Critical - Its the end of the world as we know it'),
    ]

    # Links to the authenticated User if they are logged in.
    # Set blank=True and null=True so guests can complete the form
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='support_tickets')   # noqa: E501
    # Core contact information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    # Ticket details
    subject = models.CharField(max_length=200)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES,
                                default='low')
    message = models.TextField()

    # Store a custom ticket string
    ticket_id_string = models.CharField(max_length=20, unique=True,
                                        editable=False, blank=True, null=True)

    # Status
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    resolution = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        """Add TICK to ID generation number after generation"""
        super().save(*args, **kwargs)

        if not self.ticket_id_string:
            self.ticket_id_string = f"TICK#00{self.id}"
            SupportTicket.objects.filter(id=self.id).update(ticket_id_string=self.ticket_id_string)   # noqa: E501

    def __str__(self):
        return self.ticket_id_string if self.ticket_id_string else "PENDING"
