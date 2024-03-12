from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from usuario.models import Usuario

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Livro(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    paginas = models.IntegerField(null=True, blank=True)
    autor = models.CharField(max_length=50, null=True, blank=True)
    emprestado = models.BooleanField(default=False)
    data_publicacao = models.DateField(null=True, blank=True)
    data_cadastro = models.DateField(null=True, blank=True)
    data_emprestimo = models.DateTimeField(null=True, blank=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    tempo_duracao = models.DurationField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='livros/covers/%Y/%m/%d/')
    emprestado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}" 