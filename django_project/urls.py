from django.contrib import admin
from django.urls import path
from Economation import views  

urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('noticias', views.noticias, name='noticias'),  
    path('home/', views.home, name = 'home'),
    path('artigos/', views.artigos, name='artigos'),
    path('admin/', admin.site.urls),  
    path('suporte/', views.suporte, name='suporte'),
    path('sucesso_mensagem/', views.sucesso_mensagem, name='sucesso_mensagem'),
    path('sucesso_cadastro/', views.sucesso_cadastro, name='sucesso_cadastro'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
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
    path('noticiainov/', views.NotInovacao, name='noticiainov'),
    path('login/', views.login, name='login'),
    path('esqueceusenha/', views.esqueceusenha, name='esqueceusenha'),
    path('senhanova/', views.senhanova, name='senhanova'),
    path('inicial/', views.inicial, name = 'inicial')
]