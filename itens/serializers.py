from django.contrib.auth.models import User, Group
from .models import Item, Alternativa
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
 
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
        

        
    