from django.shortcuts import render
from .models import Post


from django.http import HttpResponse

def News_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "News/News.html", context )
