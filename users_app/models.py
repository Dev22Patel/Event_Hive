

from django.db import models


class SponsorType(models.Model):
    name = models.CharField(max_length=255)


class Events(models.Model):
    lead_orgname = models.CharField(max_length=255)
    lead_orgphno = models.CharField(max_length=10)
    lead_orgphno_veri = models.BooleanField(default=False)
    eventdate = models.DateField(default=None)
    email = models.EmailField(max_length=255)
    biddate = models.DateField(default=None)
    sponsortypes = models.ManyToManyField(SponsorType)
    posterimg = models.ImageField()
    description=models.TextField()
















