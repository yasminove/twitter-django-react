from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name='twitter-home'), 
    path('about/', views.about, name='twitter-about')
]