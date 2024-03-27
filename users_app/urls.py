from django.urls import include, path
from users_app import views
from EduHub.views import Mainpage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Mainpage, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),

]
