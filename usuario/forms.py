from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
import re


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula, um número e ter no mínimo 8 caracteres.',
            code='invalid'
        )

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']


class loginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha'] 