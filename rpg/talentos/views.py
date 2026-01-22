from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Talento
from .serializers import SerializerTalento
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetTalento(viewsets.ModelViewSet):
    queryset = Talento.objects.all()
    serializer_class = SerializerTalento
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        return Talento.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)