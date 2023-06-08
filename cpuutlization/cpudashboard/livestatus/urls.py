from django.urls import include, path

from . import views
                  



urlpatterns = [
            
               #for livestatus
                path('',views.live_status, name="live_status"),
               ]