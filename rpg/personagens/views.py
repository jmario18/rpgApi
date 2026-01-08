from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Personagem
from .serializers import SerializerPersonagem
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetPersonagem(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = SerializerPersonagem
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        return Personagem.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)