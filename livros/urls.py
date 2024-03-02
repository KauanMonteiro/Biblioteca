from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/categoria/<int:category_id>/', views.category, name='category'),
    path('emprestar/<int:livro_id>/', views.emprestar_livro, name='emprestar_livro'),
    path('devolver_livro/<int:livro_id>/', views.devolver_livro, name='devolver_livro'),
]
