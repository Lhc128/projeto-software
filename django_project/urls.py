from django.contrib import admin
from django.urls import path
from Economation import views  

urlpatterns = [
    path('home/', views.home, name='home'),
    path('noticias', views.noticias, name='noticias'),  
    path('artigos/', views.artigos, name='artigos'),
    path('admin/', admin.site.urls),  
    path('suporte/', views.suporte, name='suporte'),
    path('sucesso/', views.sucesso_view, name='sucesso'),
    path('inicio/', views.inicio, name='inicio')
]