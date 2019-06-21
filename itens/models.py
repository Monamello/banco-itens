from django.db import models
from django.contrib.auth.models import User, Group

class Item(models.Model):
    DIFICULDADES = (
        ('muito_facil', 'Muito Fácil'),
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
        ('muito_dificil', 'Muito Difícil'),
    )
    
    enunciado = models.CharField(max_length=500) # Pesquisar sobre RichTextField
    suporte = models.CharField(max_length=500) # Pesquisar sobre RichTextField
    comando = models.CharField(max_length=500) # Pesquisar sobre RichTextField
    dificuldade = models.CharField(max_length=30, choices=DIFICULDADES)
    curso = models.CharField(max_length=30)
    unidade_curricular = models.CharField(max_length=45)
    autor = models.ForeignKey(User, on_delete="CASCADE")


class Alternativa(models.Model):
    texto = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='imagem_alternativas')
    correta = models.BooleanField(default=False)
    item = models.ForeignKey(Item, related_name='alternativas', on_delete="CASCADE")