from usuario.models import Usuario
from django.contrib import admin

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'ativo', 'senha')
    list_display = ('nome', 'email', 'ativo') 
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)
