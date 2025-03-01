from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=50)
    Texto = models.CharField(max_length=200)
    Lingua_Para_Tradução = models.CharField(max_length=200)
    Tradução = models.CharField(max_length=200)
    
    def __self__(self):
        f'Nome: {self.name}| Texto: {self.Texto}| Lingua Para Tradução: {self.Lingua_Para_Tradução}| Tradução: {self.Tradução}'