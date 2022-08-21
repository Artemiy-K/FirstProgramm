from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>/", views.get_category, name="get_category"),
]
