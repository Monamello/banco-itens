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
        
class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')
        
class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('__all__')
        
    