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
    
    enunciado = models.TextField(max_length=1200)
    suporte = models.TextField(max_length=1200)
    comando = models.TextField(max_length=1200)
    dificuldade = models.CharField(max_length=30, choices=DIFICULDADES)
    cursos = models.ManyToManyField('Cursos')
    #unidades_curriculares = models.ManyToManyField('UnidadeCurricular')
    unidades_curriculares = models.ForeignKey('UnidadeCurricular', related_name='unidades_curriculares', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


class Alternativa(models.Model):
    texto = models.TextField(max_length=1200)
    imagem = models.ImageField(upload_to='imagem_alternativas', blank=True, null=True)
    correta = models.BooleanField(default=False)
    item = models.ForeignKey(Item, related_name='alternativas', on_delete=models.CASCADE)


class Cursos(models.Model):
    nome = models.CharField(max_length=254)
    unidades_curriculares = models.ManyToManyField('UnidadeCurricular')
    docente = models.ManyToManyField(User)


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=254)