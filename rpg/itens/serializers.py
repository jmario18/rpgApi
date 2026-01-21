from rest_framework import serializers
from .models import Item

class SerializerItem(serializers.Serializer):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'tipo', 'sintonizacao', 'descricao']