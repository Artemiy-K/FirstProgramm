from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. path("pisa", views.pisa, name="pisa")

def index(request):
    return HttpResponse("hello world")

def pisa(request):
    return HttpResponse("<h1>TUT TAKOGO NET POKA</h1>")


def cocki(request):
    return HttpResponse("<h3>C       O        C      K      I</h3>")

