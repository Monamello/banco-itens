from .models import Item, Alternativa
from rest_framework import serializers
from accounts.serializers import UserSerializer


class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('texto', 'imagem', 'correta', 'item')
        
class ItensSerializer(serializers.ModelSerializer):
    
    alternativas = AlternativasSerializer(many=True)

    
    class Meta:
        model = Item
        fields = ('enunciado', 'suporte', 'comando', 
            'dificuldade', 'curso', 'unidade_curricular', 'alternativas')
            

        
    