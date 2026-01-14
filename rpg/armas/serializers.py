from rest_framework import serializers
from .models import Arma

class SerializerArma(serializers.Serializer):
    class Meta:
        model = Arma
        fields = ['id', 'nome', 'n_dado', 'dano', 'n_dado_ex', 'dano_ex']