
from django.contrib import admin
from django.urls import include, path
from .views import Mainpage , home,success,view_events
# from users_app.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainpage, name="index"),
    path('', success, name="success"),

    path("home/",home,name="home"),
    path('event/', include(('Eventapp.urls','Eventapp'), namespace='event')),
    path('access/', include(('users_app.urls', 'users_app'), namespace='access')),
    path('viewevents/', view_events, name='view_events'),

]