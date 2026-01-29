from rest_framework import serializers
from .models import Armadura

class SerializerArmadura(serializers.ModelSerializer):
    class Meta:
        model = Armadura
        fields = ['id', 'nome', 'tipo', 'classeDeArmadura', 'peso', 'public']