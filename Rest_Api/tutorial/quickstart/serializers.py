from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import Imovel, Cliente


class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imovel
        fields = [
            'id',
            'codigo',
            'tipo',
            'endereco',
            'valor'
        ]

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'email',
            'telefone'
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']