from rest_framework import serializers
from .models import Personagem, PersonagemArma, PersonagemArmadura
from armas.serializers import SerializerArma
from armaduras.serializers import SerializerArmadura

class SerializerPersonagemArma(serializers.ModelSerializer):
    arma = SerializerArma(read_only=True)

    class Meta:
        model = PersonagemArma
        fields = [
            'id',
            'arma',
            'quantidade',
            'equipado'
        ]

class SerializerPersonagemArmadura(serializers.ModelSerializer):
    armadura = SerializerArmadura(read_only=True)

    class Meta:
        model = PersonagemArmadura
        fields = [
            'id',
            'armadura',
            'equipado'
        ]

class SerializerPersonagem(serializers.ModelSerializer):
    armas = SerializerPersonagemArma(many = True, read_only= True)
    armaduras = SerializerPersonagemArmadura(many = True, read_only= True)

    class Meta:
        model = Personagem
        fields = [
            'id',
            'nome',
            'level',
            'armas',
            'armaduras'
            ]

