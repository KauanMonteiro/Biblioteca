from django.db import models

class Usuario(models.Model):

    ADMIN ='Admin'
    USUARIO_COMUM = 'Usuario_comum'
    CARGO_CHOICES = [
        (ADMIN,'Admin'),
        (USUARIO_COMUM,'Usuario_comum')
    ]
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=True)
    cargo = models.CharField(max_length=13, choices=CARGO_CHOICES, default=USUARIO_COMUM)

    def __str__(self) -> str:
        return self.nome
