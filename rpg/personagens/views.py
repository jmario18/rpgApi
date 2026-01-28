from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Personagem, PersonagemArma
from .serializers import SerializerPersonagem
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetPersonagem(viewsets.ReadOnlyModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = SerializerPersonagem
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        return Personagem.objects.filter(dono=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

class ViewSetPersonagemArma(viewsets.ModelViewSet):
    queryset = PersonagemArma.objects.all()
    #verificar as permissões
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def equipar(self, request, pk=None):
        cw = self.get_object()

        if cw.equipado >= cw.quantidade:
            return Response(
                {"error":"Não é possivel equipar mais armas do que você possui."},
                status=status.HTTP_400_BAD_REQUEST
            )

        cw.equipado += 1
        cw.save()

        return Response(
            {"message":"Arma equipada com sucesso."},
            status=status.HTTP_200_OK
        )