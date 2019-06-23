from .models import Item, Alternativa, Cursos, Materias
from rest_framework import serializers


class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('texto', 'imagem', 'correta', 'item')
        

class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('enunciado', 'suporte', 'comando', 
            'dificuldade', 'cursos', 'unidade_curricular', 'autor')


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos 
        fields = ('nome', 'materias')


class MateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias 
        fields = ('nome')
            

        
    