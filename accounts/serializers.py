from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, style={'input_type': 'password'})

    def create(self, validated_data):
            user = User.objects.create_user(
                    validated_data['username'], 
                    validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return user

    class Meta:
            model = User
            fields = ('id', 'username', 'password', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')