from django.db import models
from django.contrib.auth.models import User

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
    autor = models.ForeignKey(User)