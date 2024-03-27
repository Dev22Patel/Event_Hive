from django.db import models
from django.db.models import JSONField
from django import forms


class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    CoursePrice = models.DecimalField(max_digits=10, decimal_places=2)
    CourseDuration = models.CharField(max_length=100)
    TeacherName = models.CharField(max_length=100)
    course_image = models.ImageField(null=True,blank=True,upload_to= 'course_photo/')
    LastUpdated = models.DateField()
    Description = models.TextField()

    def __str__(self):
        return self.CourseName