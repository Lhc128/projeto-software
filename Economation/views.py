from django.shortcuts import render

def noticias(request):
    return render(request, 'noticias.html')  

def artigos(request):
    return render(request, 'artigos.html')  
