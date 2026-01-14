from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Arma
from .serializers import SerializerArma
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetArma(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = SerializerArma
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        return Arma.objects.filter(dono=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)