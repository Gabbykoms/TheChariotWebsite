from django.shortcuts import render

from django.http import HttpResponse


def Sponsor(request):
    return render(request,'Sponsor/Sponsor.html')



