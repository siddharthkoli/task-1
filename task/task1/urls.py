from django.urls import path
from task1 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("generateNumbers", views.generateNumbers, name="generateNumbers")
]