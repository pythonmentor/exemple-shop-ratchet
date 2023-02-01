from django.urls import path

from .views import home, detail

app_name = "exemple"

urlpatterns = [
    path('', home, name="home"),
    path('<slug:slug>/', detail, name="detail"),
]
