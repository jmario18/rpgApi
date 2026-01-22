from rest_framework import serializers
from .models import Talento

class SerializerTalento(serializers.ModelSerializer):
    class Meta:
        model = Talento
        fields = ['id', 'nome', 'tipo', 'pre_requisitos', 'descricao']