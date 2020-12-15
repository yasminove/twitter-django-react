from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'yasmin hillis', 
        'title': 'yasmin is awesome'
    },
    {
        'author':'awesome hillis', 
        'title': 'yasmin is awesome'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'library/home.html', context)


def about(request):
    return render(request, 'library/about.html', {'title': 'about!'})