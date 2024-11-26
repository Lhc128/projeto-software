from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    
class MensagensSuporte(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    mensagem = models.CharField(max_length=500)

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True, verbose_name="Criado em")


  
