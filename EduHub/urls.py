
from django.contrib import admin
from django.urls import include, path
from .views import Mainpage , home,view_events , logout_view
from django.contrib.auth import views as auth_views
from .views import index,to_cart
from django.conf import settings
from django.conf.urls.static import static
# from users_app.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainpage, name="index"),
    path('to_cart/',to_cart,name="to_cart"),
    path("home/",home,name="home"),
    path('course/', include(('Course_app.urls','Course_app'), namespace='course')),
    path('access/', include(('users_app.urls', 'users_app'), namespace='access')),
    path('viewevents/', view_events, name='view_events'),
    path('logout/', logout_view , name='logout'),
    path('index/',index,name="index"),
    path('feedback/',include(('feedback.urls','feedback'),namespace='feedback')),

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)