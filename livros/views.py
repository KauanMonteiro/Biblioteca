from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from livros.models import Livro

def home(request):
    livros = Livro.objects.all()
    return render(request, 'livros/pages/home.html', context={'livros': livros})

