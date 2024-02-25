from django.contrib import admin
from .models import Livro,Category


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Livro)
admin.site.register(Category, CategoryAdmin)