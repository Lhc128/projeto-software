from django.shortcuts import render

def noticias(request):
    return render(request, 'noticias.html')  

def artigos(request):
    return render(request, 'artigos.html')  
    
def noticiasInov(request):
    return render(request, 'noticiasInov.html')

def noticiasTec(request):
    return render(request, 'noticiasTec.html')

def noticiasFin(request):
    return render(request, 'noticiasFin.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def esqueceusenha(request):
    return render(request, 'esqueceusenha.html')

def senhanova(request):
    return render(request, 'senhanova.html')