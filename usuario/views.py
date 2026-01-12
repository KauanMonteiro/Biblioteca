from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CadastroForm, LoginForm
from django.contrib import messages
from hashlib import sha256

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['usuario'] = form.usuario.id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.senha = sha256(user.senha.encode()).hexdigest()
            user.save()
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})


def sair(request):
    request.session.flush()
    return redirect(reverse('home'))
