from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
import re
from hashlib import sha256

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula, um número e ter no mínimo 8 caracteres.',
            code='invalid'
        )

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        validators=[strong_password]
    )
    senha2 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
    )
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError(
                {'senha2':'As senhas não são iguais.'}
            )
class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha'] 
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            senha = cleaned_data.get('senha')

            if email and senha:
                senha_hashed = sha256(senha.encode()).hexdigest()
                usuario = Usuario.objects.filter(email=email, senha=senha_hashed).first()
                if not usuario:
                    raise ValidationError("Email ou senha inválidos")
                self.usuario = usuario
            return cleaned_data