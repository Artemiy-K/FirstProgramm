from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

# Create your views here.

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/index.html', {
        'news':news,
        'title': 'список новостей',
        'category': categories,
    })

    return render(request, template_name='news/index.html', context=context)