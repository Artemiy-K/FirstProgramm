from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def pisa(request):
    return HttpResponse("<h1>Ой что-то мы засиделись,братцы, не пора ли нам прогуляться? Русь молодая, силы не меренно!Дайте коня мне да добрый  меч</h1>")


def cocki(request):
    return HttpResponse("<h3>C       O        C      K      I</h3>")

