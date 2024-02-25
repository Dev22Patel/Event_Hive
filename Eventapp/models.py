from django.db import models
from django.db.models import JSONField

class Event(models.Model):
    EventName = models.CharField(max_length=255 , default ="Not specified")  # Added event_name field
    LeadOrganizerName = models.CharField(max_length=100)
    LeadOrganizerPhone = models.CharField(max_length=20)
    EventDate = models.DateField()
    LeadOrganizerEmail = models.EmailField()
    # SponsorTypes = JSONField()  
    BiddingDate = models.DateField()
    Description = models.TextField()

    def __str__(self):
        return f"{self.EventName} - {self.LeadOrganizerName}"
