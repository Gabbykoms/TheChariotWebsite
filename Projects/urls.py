from django.urls import path
from .import views


urlpatterns = [
    path('Projects', views.Projects,  name = "Projects"),



]