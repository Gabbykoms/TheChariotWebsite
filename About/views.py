from django.shortcuts import render
from django.http import HttpResponse 


def About_us(request):
    return render(request,'About/About_us.html')

def About_team(request):
    return render(request,'About/About_team.html')

def About_volunteering(request):
    return render(request,'About/About_volunteering.html')

def About_tokens(request):
    return render(request,'About/About_tokens.html')