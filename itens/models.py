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
    cursos = models.ManyToManyField('Cursos')
    unidade_curricular = models.CharField(max_length=45)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


class Alternativa(models.Model):
    texto = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='imagem_alternativas')
    correta = models.BooleanField(default=False)
    item = models.ForeignKey(Item, related_name='alternativas', on_delete=models.CASCADE)


class Cursos(models.Model):
    nome = models.CharField(max_length=254)
    materias = models.ManyToManyField('Materias')
    docente = models.ManyToManyField(User)


class Materias(models.Model):
    nome = models.CharField(max_length=254)