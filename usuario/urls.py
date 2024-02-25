from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.valida_cadastro, name='cadastro'),
    path('login/', views.validar_login, name='login'),
    path('logout/', views.sair, name='logout'),
]
