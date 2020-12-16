from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'yasmin hillis', 
        'title': 'yasmin is awesome', 
        'date_posted': '24, September, 2021', 
        'content': 'Blog post 1'
    },
    {
        'author':'awesome hillis', 
        'title': 'yasmin is awesome',
        'date_posted': '25, September, 2021', 
        'content': 'Blog post 2'
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