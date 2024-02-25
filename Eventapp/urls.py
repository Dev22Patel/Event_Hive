# Eventapp/urls.py

from django.urls import path
from .views import add_event  # Make sure this import matches your view function

app_name = 'Eventapp'  # This line is not necessary when using the `namespace` argument in `include()`

urlpatterns = [
    path('add/', add_event, name='add_event'),  # Ensure this name matches what you use in the template
]
