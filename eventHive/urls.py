
from django.contrib import admin
from django.urls import include, path
from .views import Mainpage , home
# from users_app.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainpage, name="index"),
    path("home/",home,name="home"),

    path('access/', include(('users_app.urls', 'users_app'), namespace='access')),

]