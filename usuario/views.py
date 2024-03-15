from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Usuario
from hashlib import sha256

def login(request):
    if request.session.get('usuario'):
        return redirect('/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        usuario = Usuario.objects.filter(email=email)

        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect(reverse('cadastro') + '?status=1')

        if len(senha) < 8:
            return redirect(reverse('cadastro') + '?status=2')

        if usuario.exists():
            return redirect(reverse('cadastro') + '?status=3')

        try:
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(nome=nome, senha=senha, email=email)
            usuario.save()

            return redirect(reverse('cadastro') + '?status=0')
        except Exception as e:
            print(e)  # Handle the exception properly
            return redirect(reverse('cadastro') + '?status=4')

    return redirect(reverse('cadastro'))

def validar_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        senha_hashed = sha256(senha.encode()).hexdigest()

        usuario = Usuario.objects.filter(email=email, senha=senha_hashed).first()

        if usuario:
            request.session['usuario'] = usuario.id
            return redirect('/')
        else:
            return redirect(reverse('login') + '?status=1')

    return redirect(reverse('login'))

def sair(request):
    request.session.flush()
    return redirect(reverse('home'))
