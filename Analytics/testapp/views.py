from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return render(request, 'testapp/home.html')


def About(request):
    return render(request, 'testapp/about.html')
