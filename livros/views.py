from django.shortcuts import render
from django.http import HttpResponse
from livros.models import Livro, Category
from datetime import datetime, timedelta
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario

def home(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    livros = Livro.objects.all()
    return render(request, 'livros/pages/home.html', context={'livros': livros, 'usuario':usuario})

def category(request, category_id):
    if 'usuario' not in request.session:
        return redirect('login')
    categoria = Category.objects.get(pk=category_id)
    livros = Livro.objects.filter(category=categoria)
    return render(request, 'livros/pages/category.html', context={'livros': livros})

def livros_por_categoria(request, categoria_id):
    if 'usuario' not in request.session:
        return redirect('login')
    categoria = Category.objects.get(pk=categoria_id)
    livros = Livro.objects.filter(category=categoria)
    return render(request, 'livros/pages/livros_por_categoria.html', {'livros': livros, 'categoria': categoria})

def area_usuario(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    livros_emprestados = Livro.objects.filter(emprestado_por=usuario)
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

    if usuario.cargo == 'Admin':
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            paginas = request.POST.get('paginas')
            autor = request.POST.get('autor')
            data_publicacao = request.POST.get('data_publicacao')
            category_ids = request.POST.getlist('category') 
            cover = request.FILES.get('cover')
            
            livro = Livro.objects.create(
                titulo=titulo,
                descricao=descricao,
                paginas=paginas,
                autor=autor,
                data_publicacao=data_publicacao,
                cover=cover,
            )
            
            for category_id in category_ids:
                category = get_object_or_404(Category, id=category_id)
                livro.category.add(category)
        
        return render(request, 'livros/pages/cadastro_livro.html', {'categories': categories})

def area_admin(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session.get('usuario')
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if usuario.cargo == 'Admin':
        livros = Livro.objects.all()
        usuarios = Usuario.objects.all()
        return render(request,'livros/pages/admin.html',{'livros':livros, 'usuario':usuarios})
    
def excluir_livro(request, livro_id):
    livro = Livro.objects.get(pk = livro_id)

    if request.method == 'POST':
        livro.delete()
        return redirect('area_admin')
    
def excluir_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk = usuario_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('area_admin')

def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        paginas = request.POST.get('paginas')
        autor = request.POST.get('autor')
        data_publicacao = request.POST.get('data_publicacao')
        category_ids = request.POST.getlist('category')
        cover = request.FILES.get('cover')

        livro.titulo = titulo
        livro.descricao = descricao
        livro.paginas = paginas
        livro.autor = autor
        livro.data_publicacao = data_publicacao
        livro.cover = cover

        livro.category.set(Category.objects.filter(id__in=category_ids))

        livro.save()
        return redirect('home')

    categories = Category.objects.all()
    
    return render(request, 'livros/pages/editar_livro.html', {
        'livro': livro,
        'categories': categories
    })