from django.db import models
from django.db.models import JSONField
from django import forms
# class Event(models.Model):
#     EventName = models.CharField(max_length=255 , default ="Not specified")  # Added event_name field
#     LeadOrganizerName = models.CharField(max_length=100)
#     LeadOrganizerPhone = models.CharField(max_length=20)
#     EventDate = models.DateField()
#     LeadOrganizerEmail = models.EmailField()
#     # SponsorTypes = JSONField()  
#     BiddingDate = models.DateField()
#     Description = models.TextField()

#     def __str__(self):
#         return f"{self.EventName} - {self.LeadOrganizerName}"

class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    CoursePrice = models.DecimalField(max_digits=10, decimal_places=2)
    CourseDuration = models.CharField(max_length=100)
    TeacherName = models.CharField(max_length=100)
    course_files = models.FileField(null=True,upload_to='course_materials/')
    course_image = models.ImageField(null=True,blank=True,upload_to= 'images/')
    LastUpdated = models.DateField()
    Description = models.TextField()

    def __str__(self):
        return self.CourseName