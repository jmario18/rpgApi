from rest_framework import serializers
from .models import Item

class SerializerItem(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'tipo', 'sintonizacao', 'descricao']