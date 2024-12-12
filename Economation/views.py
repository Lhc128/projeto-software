from django.shortcuts import render, redirect
from django import forms
from .models import MensagensSuporte, Cadastro
from .forms import CadastroForm
from django.contrib.auth.models import User
from django.contrib import messages


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
            return redirect('sucesso_mensagem') 
    else:
        form = MensagemSuporte()  
    return render(request, 'suporte.html', {'form': form})

def noticias(request):
    return render(request, 'noticias.html')

def artigos(request):
    return render(request, 'artigos.html')

def sucesso_mensagem(request):
    return render(request, 'sucesso_mensagem.html')

def inicio(request):
    return render(request, 'inicio.html')

def home(request):
    return render(request,'home.html')

def jogos(request):
    return render(request,'jogos.html')

def editarperfil(request):
    return render(request,'editarperfil.html')

def perfil(request):
    return render(request,'perfil.html')

def NotInovacao(request):
    return render(request,'noticiasInov.html')

def NotFinancas(request):
    return render(request,'noticiasFin.html')

def NotTecnologia(request):
    return render(request,'noticiasTec.html')

def esqueceuSenha(request):
    return render(request,'esqueceusenha.html')

def senhanova(request):
    return render(request,'senhanova.html')

def login(request):
    return render(request,'login.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário no banco de dados
            return redirect('sucesso_cadastro')  # Redireciona para a página de sucesso
    else:
        form = CadastroForm()  # Cria um formulário vazio
    return render(request, 'cadastro.html', {'form': form})

def jogoFin(request):
    return render(request, 'jogofin.html')

def jogoInov(request):
    return render(request, 'jogoinov.html')

def jogoTec(request):
    return render(request, 'jogotec.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')

def esqueceusenha(request):
    return render(request, 'esqueceusenha.html')

def senhanova(request):
    return render(request, 'senhanova.html')

def sucesso_cadastro(request):
    return render(request, 'sucesso_cadastro.html')