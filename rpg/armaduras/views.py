from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Armadura
from .serializers import SerializerArmadura
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetArmadura(viewsets.ModelViewSet):
    queryset = Armadura.objects.all()
    serializer_class = SerializerArmadura
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        return Armadura.objects.filter(dono=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)