from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Item
from .serializers import SerializerItem
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetItem(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = SerializerItem
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        return Item.objects.filter(dono=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)