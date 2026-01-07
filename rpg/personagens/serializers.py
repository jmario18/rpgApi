from rest_framework import serializers
from .models import Personagem

class SerializerPersonagem(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = 'id', 'nome', 'level'