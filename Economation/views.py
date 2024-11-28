from django.shortcuts import render, redirect
from django import forms
from .models import MensagensSuporte

class MensagemSuporte(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=20)
    mensagem = forms.CharField(widget=forms.Textarea)

def suporte(request):
    if request.method == 'POST':
        form = MensagemSuporte(request.POST)
        if form.is_valid():
            MensagensSuporte.objects.create(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                telefone=form.cleaned_data['telefone'],
                mensagem=form.cleaned_data['mensagem']
            )
            return redirect('sucesso')  # Redireciona após o envio com sucesso
    else:
        form = MensagemSuporte()  # Cria um formulário vazio para GET
    return render(request, 'suporte.html', {'form': form})

def noticias(request):
    return render(request, 'noticias.html')

def artigos(request):
    return render(request, 'artigos.html')

def sucesso_view(request):
    return render(request, 'sucesso.html')
