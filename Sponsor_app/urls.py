from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_active_sponsor, name='add_active_sponsor'),
]
