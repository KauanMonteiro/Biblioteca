from django import forms
from django.core.exceptions import ValidationError
from .models import Livro, Avaliacao, Denuncia

class CadastroLivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'paginas','category', 'descricao','data_publicacao', 'cover',]
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'}),
        }

class EditarLivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'paginas','category', 'descricao','data_publicacao', 'cover',]
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'}),
        }

        def init(self, *args, **kwargs):
            super().init(*args, **kwargs)
            
            self.fields['cover'].required = False

class CriarAvaliacao(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota','comentario']

class Denuncia(forms.ModelForm):
    class Meta:
        models= Denuncia