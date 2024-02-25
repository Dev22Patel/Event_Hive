from django.db import models

class ActiveSponsor(models.Model):
    BrandName = models.CharField(max_length=100)
    BrandType = models.CharField(max_length=100)
    SponsorPhone = models.CharField(max_length=15)
    SponsorEmail = models.EmailField()

    def __str__(self):
        return self.BrandName
