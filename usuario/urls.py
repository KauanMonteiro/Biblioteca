from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('sair/', views.sair, name = 'sair')
    
]