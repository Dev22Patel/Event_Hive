# eventApp/models.py

from django.db import models

class Event(models.Model):
    organizer_name = models.CharField(max_length=100)
    organizer_phone = models.CharField(max_length=20)
    event_date = models.DateField()
    email = models.EmailField()
    sponsor_types = models.CharField(max_length=200)  # Consider a more structured approach for multiple choices
    bidding_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.organizer_name
