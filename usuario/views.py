from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import usuario
from hashlib import sha256

def login(request):
    if request.session.get('usuario'):
        return redirect('/livro/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/livro/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario_obj = usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/usuario/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/usuario/cadastro/?status=2')

    if usuario_obj.exists():
        return redirect('/usuario/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario_obj = usuario(nome=nome,
                              senha=senha,
                              email=email)
        usuario_obj.save()
        return redirect('/usuario/cadastro/?status=0')
    except Exception as e:
        print(e)
        return redirect('/usuario/cadastro/?status=4')

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario_obj = usuario.objects.filter(email=email, senha=senha)

    if usuario_obj.exists():
        request.session['usuario'] = usuario_obj.first().id
        return redirect('/livro/home/')
    else:
        return redirect('/usuario/login/?status=1')

def sair(request):
    request.session.flush()
    return redirect('/usuario/login/')
