from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/categoria/<int:category_id>/', views.category, name='category'),
    path('livros/por_categoria/<int:categoria_id>/', views.livros_por_categoria, name='livros_por_categoria'),
    path('emprestar/<int:livro_id>/', views.emprestar_livro, name='emprestar_livro'),
    path('devolver_livro/<int:livro_id>/', views.devolver_livro, name='devolver_livro'),
    path('area_usuario/', views.area_usuario, name='area_usuario'),
    path('search/', views.search, name='search'),
    path('area_admin/',views.area_admin, name='area_admin'),
    path('cadastro_livro/', views.cadastrar_livro, name="cadastrar_livro"),
    path('deletar_livro/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),
    path('deletar_usuario/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('editar_livro/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('ver_mais/<int:livro_id>/', views.ver_mais, name='ver_mais'),
    path('avaliar_livro/<int:livro_id>/', views.criar_avaliacao, name='avaliar_livro'),
]
