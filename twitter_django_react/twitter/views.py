from django.shortcuts import render
from .models import Post

def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'twitter/home.html', context)

def about(request):
    
    return render(request, 'twitter/about.html', {'title': 'ABOUT'})