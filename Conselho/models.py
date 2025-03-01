from django.db import models

# Create your models here.
class conselhos(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()


    def __str__(self):
        return self('nome' + '' + self.texto)