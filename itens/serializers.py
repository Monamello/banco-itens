from .models import Item, Alternativa
from rest_framework import serializers


class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('texto', 'imagem', 'correta', 'item')
        
class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('enunciado', 'suporte', 'comando', 
            'dificuldade', 'curso', 'unidade_curricular', 'autor')
            

        
    