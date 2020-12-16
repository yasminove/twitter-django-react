from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'yasmin hillis', 
        'title': 'How to upskill you career in 2021', 
        'content': 'blog post content', 
        'date_posted': '23, Aug, 2020'
    },
    {
        'author':'sam hillis', 
        'title': '10 places to visit in 2021', 
        'content': 'blog post content', 
        'date_posted': '25, Aug, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'clinic/home.html', context)

def about(request):
    return render(request, 'clinic/about.html', {'title': 'about'})    