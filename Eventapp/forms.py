from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['CourseName', 'CoursePrice', 'CourseDuration', 'TeacherName','course_files', 'course_image', 'LastUpdated', 'Description']



