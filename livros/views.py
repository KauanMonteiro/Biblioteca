from django.shortcuts import render
from django.http import HttpResponse
from livros.models import Livro,Category

def home(request):
    livros = Livro.objects.all()
    return render(request, 'livros/pages/home.html', context={'livros': livros})

def category(request, category_id):
    livros = Livro.objects.filter(
    )
    return render(request, 'livros/pages/category.html', context={'livros': livros})



def livros_por_categoria(request, categoria_id):
    categoria = Category.objects.get(pk=categoria_id)
    livros = Livro.objects.filter(category=categoria)
    return render(request, 'livros_por_categoria.html', {'livros': livros, 'categoria': categoria})
