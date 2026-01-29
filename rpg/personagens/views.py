from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Personagem, PersonagemArma, PersonagemArmadura
from .serializers import SerializerPersonagem, SerializerArma
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
    permission_classes = [IsAuthenticated, EhDonoOuAdmin]

    @action(detail=True, methods=['post'])
    def equipar(self, request, pk=None):
        # get object pega o objeto PersonagemArma
        personagem_arma = self.get_object()
        soma = 0
        personagem = personagem_arma.personagem
        for c in personagem.armas.all():
            # c == PersonagemArma, pegar valores equipado
            soma += c.equipado

        if soma >=2:
            return Response(
                {"error":"Não é possivel equipar mais do que 2 armas."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if personagem_arma.equipado >= personagem_arma.quantidade:
            return Response(
                {"error":"Não é possivel equipar mais armas do que você possui."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        personagem_arma.equipado += 1
        personagem_arma.save()

        return Response(
            {"message":"Arma equipada com sucesso."},
            status=status.HTTP_200_OK
        )
    @action(detail=True, methods=['post'])
    def desequipar(self, request, pk=None):
        personagem_arma = self.get_object()

        if personagem_arma.equipado > personagem_arma.quantidade:
            return Response(
                {"error":"Não é possivel desequipar mais armas do que você possui."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if personagem_arma.equipado == 0:
            return Response(
                {"error":"Não é possivel desequipar uma arma que não está equipada"}
            )

        personagem_arma.equipado -= 1
        personagem_arma.save()

        return Response(
            {"message":"Arma desequipada com sucesso."},
            status=status.HTTP_200_OK
        )
    
class ViewSetPersonagemArmadura(viewsets.ModelViewSet):
    queryset = PersonagemArmadura.objects.all()
    permission_classes = [IsAuthenticated, EhDonoOuAdmin]

    @action(detail=True, methods=['post'])
    def equipar(self, request, pk=None):
        personagem_armadura = self.get_object()
        eq = False
        for a in personagem_armadura.personagem.armaduras.all():
            if a.equipado == True:
                eq = True

        if eq:
            return Response(
                {"error":"Não é possivel equipar outra armadura"}
            )
        
        if personagem_armadura.equipado >=1:
            return Response(
                {"error":"Não é possivel equipar essa armadura mais de uma vez."}
            )
        
        personagem_armadura.equipado = True
        personagem_armadura.save()

        return Response(
            {"message":"Armadura equipada com sucesso!"}
        )
    
    @action(detail=True, methods=['post'])
    def desequipar(self, request, pk=None):
        personagem_armadura = self.get_object()
        if not personagem_armadura.equipado:
            return Response(
                {"error":"Você não está com essa armadura equipada!"}
            )

        personagem_armadura.equipado = False
        personagem_armadura.save()
        
        return Response(
            {"message":"Armadura desequipada com sucesso!"}
        )

