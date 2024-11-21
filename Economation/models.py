from django.db import models

class Fisiculturistas(models.Model):
  atleta = models.CharField(max_length=50)
  titulos = models.IntegerField()
  
