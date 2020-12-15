from django.shortcuts import render


posts = [
    {
        'author': "Yasmin Hillis", 
        'title': "Blog post 1", 
        'content': 'blog post content', 
        'date_posted': '23 Dec, 2020'
    }, 
    {
        'author': "Yazan Hillis", 
        'title': "Blog post 2", 
        'content': 'blog post content 2', 
        'date_posted': '25 Dec, 2020'
    },
    {
        'author': "Yazan Hillis", 
        'title': "Blog post 3", 
        'content': 'blog post content 3', 
        'date_posted': '25 Dec, 2020'
    }
]

def Home(request):
    context = {
        'posts': posts
    }
    return render(request, 'twitter/home.html', context)

def about(request):
    
    return render(request, 'twitter/about.html', {'title': 'ABOUT'})