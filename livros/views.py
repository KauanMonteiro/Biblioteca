from django.shortcuts import render
from django.http import HttpResponse
from livros.models import Livro, Category
from datetime import datetime, timedelta
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    livros = Livro.objects.all()
    return render(request, 'livros/pages/home.html', context={'livros': livros})

def category(request, category_id):
    categoria = Category.objects.get(pk=category_id)
    livros = Livro.objects.filter(category=categoria)
    return render(request, 'livros/pages/category.html', context={'livros': livros})

def livros_por_categoria(request, categoria_id):
    categoria = Category.objects.get(pk=categoria_id)
    livros = Livro.objects.filter(category=categoria)
    return render(request, 'livros_por_categoria.html', {'livros': livros, 'categoria': categoria})

def emprestar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if not livro.emprestado:
        livro.emprestado = True
        # Definindo a data de empréstimo como a data atual
        livro.data_emprestimo = datetime.now()
        # Definindo a data de devolução como 7 dias após a data de empréstimo
        livro.data_devolucao = livro.data_emprestimo + timedelta(days=7)
        livro.save()
        return redirect(reverse('home'))
    else:
        # Aqui você pode redirecionar para uma página de erro ou exibir uma mensagem informando que o livro já está emprestado
        return redirect(reverse('home'))
    

def devolver_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if livro.emprestado:
        livro.emprestado = False
        livro.save()
        return redirect(reverse('home'))
    else:
        # Here you can redirect to an error page or display a message indicating that the book is already available
        return HttpResponse("Este livro já está disponível para empréstimo.")
