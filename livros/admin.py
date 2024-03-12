from django.contrib import admin
from .models import Livro, Category

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'emprestado', 'emprestado_por')  # Exibe esses campos na lista de livros
    list_filter = ('emprestado', 'category')  # Adiciona filtros por emprestado e categoria
    search_fields = ('titulo', 'autor')  # Adiciona campo de pesquisa por título e autor

admin.site.register(Livro, LivroAdmin)
admin.site.register(Category)
