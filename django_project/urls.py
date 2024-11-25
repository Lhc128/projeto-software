from django.contrib import admin
from django.urls import path
from Economation import views  

urlpatterns = [
    path('', views.noticias, name='noticias'),  
    path('artigos/', views.artigos, name='artigos'),
    path('admin/', admin.site.urls),  
    path('suporte/', views.suporte, name='suporte'),
]
