from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.

def index(request):
    news = News.objects.all()
    res = '<h1>Cпиисок новостей</h1>'
    
    return HttpResponse("hello world")
