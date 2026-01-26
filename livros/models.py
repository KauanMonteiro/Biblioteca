from django.db import models
from usuario.models import Usuario

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Livro(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(null=True, blank=True)
    paginas = models.IntegerField(null=True, blank=True)
    autor = models.CharField(max_length=50, null=True, blank=True)
    emprestado = models.BooleanField(default=False)
    data_publicacao = models.DateField(null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True,null=True, blank=True)
    data_emprestimo = models.DateTimeField(null=True, blank=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='livros/covers/%Y/%m/%d/')
    emprestado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    deletado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {self.autor}" 

class Avaliacao(models.Model):
    NOTAS = [(i, i) for i in range(6)]  

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=NOTAS)
    comentario = models.TextField(null=True, blank=True)
    data_avaliacao = models.DateField(auto_now_add=True)
    denuncias_count = models.PositiveIntegerField(default=0)
    deletado = models.BooleanField(default=False)
    def __str__(self):
        return f"Avaliação de {self.usuario.nome} para {self.livro.titulo}"

class Denuncia(models.Model):
    MOTIVOS=[
        ('SPAM', 'Conteúdo inadequado'),
        ('OFENSIVO', 'Linguagem ofensiva'),
        ('FALSO', 'Informação falsa'),
        ('OUTRO', 'Outro motivo'),
    ]

    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    motivo = models.CharField((""),choices=MOTIVOS)
    comentario = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Denúncia por {self.usuario} em {self.reclamacao.titulo}"