from .models import Item, Alternativa
from rest_framework import serializers
from accounts.serializers import UserSerializer


class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('__all__')
        
class ItensSerializer(serializers.ModelSerializer):
    
    alternativas = AlternativasSerializer(many=True, read_only=True)
    autor = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = Item
        fields = ('__all__')
        

        
    