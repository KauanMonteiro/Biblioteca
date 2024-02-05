from django.urls import path
from django.http import HttpResponse
from livros.views import home

urlpatterns = [
    path('',home),
]