from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("pisa", views.pisa, name="pisa"),
    path("cocki", views.cocki, name="cocki")


]