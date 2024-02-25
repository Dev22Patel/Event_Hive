from django.db import models
# Use the core JSONField for compatibility with SQLite
from django.db.models import JSONField

class Event(models.Model):
    LeadOrganizerName = models.CharField(max_length=100)
    LeadOrganizerPhone = models.CharField(max_length=20)
    EventDate = models.DateField()
    LeadOrganizerEmail = models.EmailField()
    # For sponsor types, consider storing them as a list or a JSON structure if multiple selections are allowed
    # SponsorTypes = JSONField()  # Adjust how you handle sponsor types based on your form and requirements
    BiddingDate = models.DateField()
    Description = models.TextField()

    def __str__(self):
        return self.LeadOrganizerName
