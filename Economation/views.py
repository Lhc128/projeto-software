from django.shortcuts import render
from .models import User, MensagensSuporte, Cadastro

def noticias(request):
    return render(request, 'noticias.html')  

def artigos(request):
    return render(request, 'artigos.html')  

def suporte(request):
    return render(request, 'suporte.html')

def inicial(request):
    return render(request, 'inicial.html')
