from django.shortcuts import render
from django.http import HttpResponse

def store(request):
    return HttpResponse('<h2>Store</h2>')

