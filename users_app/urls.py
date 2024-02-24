from django.urls import include, path
from users_app import views
from eventHive.views import Mainpage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Mainpage, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),

]
#    path('', Mainpage, name="index"),
#     path('register/', views.register, name="register"),
#     path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
