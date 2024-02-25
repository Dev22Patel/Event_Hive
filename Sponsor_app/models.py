from django.db import models

class ActiveSponsor(models.Model):
    SponserName = models.CharField(max_length=100)
    SponserType = models.CharField(max_length=100)
    SponserPhone = models.CharField(max_length=15)
    SponserEmail = models.EmailField()

    def __str__(self):
        return self.SponserName
