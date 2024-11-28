from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
class MensagensSuporte(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField()

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True, verbose_name="Criado em")


  
