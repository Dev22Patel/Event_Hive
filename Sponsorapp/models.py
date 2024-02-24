from django.db import models


class Sponsors(models.Model):
    Name = models.CharField(max_length=255)
    phne_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    phno_verified = models.BooleanField(default=False)








