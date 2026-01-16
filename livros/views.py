from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from livros.models import Livro, Category
from datetime import datetime, timedelta
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario
from django.contrib import messages
from .forms import CadastroLivroForm,EditarLivroForm,CriarAvaliacao

def home(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    livros = Livro.objects.all().exclude(deletado = True)
    return render(request, 'livros/pages/home.html', context={'livros': livros, 'usuario':usuario})

def category(request, category_id):
    if 'usuario' not in request.session:
        return redirect('login')
    categoria = Category.objects.get(pk=category_id)
    livros = Livro.objects.filter(category=categoria).exclude(deletado = True)
    return render(request, 'livros/pages/category.html', context={'livros': livros})

def livros_por_categoria(request, categoria_id):
    if 'usuario' not in request.session:
        return redirect('login')
    categoria = Category.objects.get(pk=categoria_id)
    livros = Livro.objects.filter(category=categoria).exclude(deletado = True)
    return render(request, 'livros/pages/livros_por_categoria.html', {'livros': livros, 'categoria': categoria})

def area_usuario(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    livros_emprestados = Livro.objects.filter(emprestado_por=usuario).exclude(deletado = True)
    return render(request, 'livros/pages/area_usuario.html', {'livros_emprestados': livros_emprestados, 'usuario': usuario})

def emprestar_livro(request, livro_id):
    if 'usuario' not in request.session:
        return redirect('login')

    livro = get_object_or_404(Livro, pk=livro_id)
    if not livro.emprestado:
        livro.emprestado = True
        livro.data_emprestimo = datetime.now()
        usuario_id = request.session['usuario']
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        livro.emprestado_por = usuario
        livro.save()
        return redirect(reverse('home'))
    else:
        return redirect(reverse('home'))

def devolver_livro(request, livro_id):
    if 'usuario' not in request.session:
        return redirect('login')

    livro = get_object_or_404(Livro, pk=livro_id)
    if livro.emprestado and livro.emprestado_por_id == request.session['usuario']:
        livro.emprestado = False
        livro.emprestado_por = None  
        livro.save()
        return redirect(reverse('home'))
    else:
        return HttpResponse("Você não pode devolver este livro.")
    
def search(request):
    if 'search' in request.GET:
        query = request.GET['search']
        livros = Livro.objects.filter(titulo__icontains=query)
        return render(request, 'livros/pages/search_results.html', {'livros': livros, 'query': query})
    else:
        return redirect(reverse('home'))
    
def cadastrar_livro(request):
    categories = Category.objects.all()

    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = CadastroLivroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('area_admin')
        else:
            messages.error(request, 'Por favor, corrija os erros.')
    else:
        form = CadastroLivroForm()
    return render(request, 'livros/pages/cadastro_livro.html', {'form': form})

def area_admin(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if usuario.cargo == 'Admin':
        livros = Livro.objects.all().exclude(deletado = True)
        usuarios = Usuario.objects.all().exclude(ativo = False)
        return render(request,'livros/pages/admin.html',{'livros':livros, 'usuario':usuarios})
    
def excluir_livro(request, livro_id):
    livro = Livro.objects.get(pk = livro_id)

    if request.method == 'POST':
        livro.deletado = True
        livro.save()
        return redirect('area_admin')
    
def excluir_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk = usuario_id)

    if request.method == 'POST':
        usuario.ativo = False
        usuario.save()
        return redirect('area_admin')

def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        form = EditarLivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('area_admin')
        else:
            messages.error(request, 'Por favor, corrija os erros.') 
    else:
        form = EditarLivroForm(instance=livro)
    return render(request, 'livros/pages/editar_livro.html', {
        'form': form,
        'livro': livro
    })

def ver_mais(request, livro_id):
    if 'usuario' not in request.session:
        return redirect('login')
    
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'livros/pages/vermais.html', {'livro': livro})

def criar_avaliacao(request,livro_id):
    if 'usuario' not in request.session:
        return redirect('login')
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == 'POST':
        form = CriarAvaliacao(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.livro = livro
            avaliacao.usuario = usuario
            avaliacao.save()
            messages.success(request, 'Avaliação cadastrado com sucesso!')
            return home
        else:
            messages.error(request, 'Por favor, corrija os erros.')
    else:
        form = CriarAvaliacao()
    return render(request, 'livros/pages/criar_avaliacao.html',{'livro':livro,'form':form})