from django.urls import path  
from .views import feedback,show_review  
  
urlpatterns = [  
    path('review/', feedback, name="feedback_form"),
    path('show/',show_review,name="show_img"),  
]