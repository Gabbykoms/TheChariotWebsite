from django.shortcuts import render

from django.http import HttpResponse

# def Projects(request):
#     return HttpResponse('<h1>Projects page </h1>')

def Projects(request):
    return render(request,"Projects/projects.html")

