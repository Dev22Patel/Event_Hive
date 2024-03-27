# Eventapp/urls.py

from django.urls import path
from .views import add_course,course_form # Make sure this import matches your view function

app_name = 'Eventapp'  # This line is not necessary when using the `namespace` argument in `include()`

urlpatterns = [
    path('add/', add_course, name='add_course'),  # Ensure this name matches what you use in the template
    path('course_form',course_form,name="course_form"),
]
