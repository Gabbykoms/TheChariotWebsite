from django.urls import path

from .import views
from .views import About_us

urlpatterns = [
    path('About_us', About_us, name = "About_us"),
    path('About_team', views.About_team, name = "About_team"),
    path('About_volunteering', views.About_volunteering, name = "About_volunteering"),
    path('About_tokens', views.About_tokens, name = "About_tokens"),



]