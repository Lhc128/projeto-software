from django.contrib import admin
from django.urls import path
from Economation import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('noticias', views.noticias, name='noticias'),  
    path('artigos/', views.artigos, name='artigos'),
    path('admin/', admin.site.urls),  
    path('suporte/', views.suporte, name='suporte'),
    path('sucesso/', views.sucesso_view, name='sucesso'),
    path('inicio/', views.inicio, name='inicio'),
    path('jogos/', views.jogos, name='jogos'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editarperfil, name='editar-perfil'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('jogotec/', views.jogoTec, name='jogotec'),
    path('jogoinov/', views.jogoInov, name='jogoinov'),
    path('jogofin/', views.jogoFin, name='jogofin'),
    path('noticiatec/', views.NotTecnologia, name='noticiatec'),
    path('noticiafin/', views.NotFinancas, name='noticiafin'),
    path('noticiainov/', views.NotInovacao, name='noticiainov')
]