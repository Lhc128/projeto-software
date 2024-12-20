"""
URL configuration for economation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_economation import views  

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('artigos/', views.artigos, name='artigos'),
    path('noticiasInov/', views.noticiasInov, name='noticiasInov'),
    path('noticiasTec/', views.noticiasTec, name='noticiasTec'),
    path('noticiasFin/', views.noticiasFin, name='noticiasFin'),
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('esqueceusenha/', views.esqueceusenha, name='esqueceusenha'),
    path('senhanova/', views.senhanova, name='senhanova'),

]

