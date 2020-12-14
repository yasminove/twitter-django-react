from django.shortcuts import render

from django.http import HttpResponse

def Home(request):
    return HttpResponse('<h1>Twitter Home</h1>')

def about(request):
    return HttpResponse('<h2>Twitter About</h2>')    