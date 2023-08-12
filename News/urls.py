from django.urls import path

from. import views

urlpatterns = [
#    <!-- path('', views.News, name = "News")-->
    path('posts/', views.News_posts, name='News_posts'),

]