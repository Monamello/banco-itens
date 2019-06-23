from .models import Item, Alternativa, Cursos, UnidadeCurricular
from rest_framework import serializers

        
class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('enunciado', 'suporte', 'comando', 
            'dificuldade', 'cursos', 'unidade_curricular', 'autor')


class AlternativasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternativa
        fields = ('texto', 'imagem', 'correta', 'item')


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos 
        fields = ('nome', 'unidade_curricular')


class UnidadeCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular 
        fields = ('nome')