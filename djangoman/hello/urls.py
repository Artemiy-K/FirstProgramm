from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls"))
]