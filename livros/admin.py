from django.contrib import admin
from .models import Livro, Category,Avaliacao

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'emprestado', 'emprestado_por')  
    list_filter = ('emprestado', 'category')  
    search_fields = ('titulo', 'autor')

admin.site.register(Livro, LivroAdmin)
admin.site.register(Category)
admin.site.register(Avaliacao)
