# views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from hashlib import sha256
from .models import Usuario

def home(request):
    return render(request, 'livros/home.html')

def valida_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        if not nome.strip() or not email.strip() or not senha.strip():
            context = {'status': 'Por favor, preencha todos os campos.'}
            return render(request, 'cadastro.html', context)

        if len(senha) < 8:
            context = {'status': 'A senha deve ter pelo menos 8 caracteres.'}
            return render(request, 'cadastro.html', context)

        if Usuario.objects.filter(email=email).exists():
            context = {'status': 'Já existe um usuário com este e-mail.'}
            return render(request, 'cadastro.html', context)

        try:
            senha = sha256(senha.encode()).hexdigest()
            usuario_obj = Usuario.objects.create(nome=nome, senha=senha, email=email)
            context = {'status': 'Cadastro realizado com sucesso. Faça o login para acessar sua conta.'}
            return redirect(reverse('login'))
        except Exception as e:
            print(e)
            context = {'status': 'Ocorreu um erro ao cadastrar o usuário.'}
            return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html')

def validar_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha = sha256(senha.encode()).hexdigest()

        usuario_obj = Usuario.objects.filter(email=email, senha=senha).first()
        if usuario_obj:
            request.session['usuario'] = usuario_obj.id
            return redirect(reverse('home'))
        else:
            context = {'status': 'E-mail ou senha incorretos.'}
            return render(request, 'login.html', context)

    return render(request, 'login.html')

def sair(request):
    request.session.flush()
    return redirect(reverse('login'))
