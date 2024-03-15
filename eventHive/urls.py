
from django.contrib import admin
from django.urls import include, path
from .views import Mainpage , home,view_events , logout_view,view_sponsors
from django.contrib.auth import views as auth_views

# from users_app.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainpage, name="index"),

    path("home/",home,name="home"),
    path('event/', include(('Eventapp.urls','Eventapp'), namespace='event')),
    path('sponsor/',include(('Sponsor_app.urls','Sponsor_app'),namespace="sponsor")),
    path('access/', include(('users_app.urls', 'users_app'), namespace='access')),
    path('viewevents/', view_events, name='view_events'),
    path('viewsponsors/', view_sponsors, name='view_sponsors'),
    path('logout/', logout_view , name='logout'),


]