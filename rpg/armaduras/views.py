from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Armadura
from .serializers import SerializerArmadura
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetArmadura(viewsets.ModelViewSet):
    queryset = Armadura.objects.all()
    serializer_class = SerializerArmadura
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        # return armaduras owned by the user or marked as public
        return Armadura.objects.filter(Q(dono=self.request.user) | Q(public=True))
    
    def perform_create(self, serializer):
        # prevent non-staff users from creating public armors
        if not self.request.user.is_staff:
            serializer.save(dono=self.request.user, public=False)
        else:
            serializer.save(dono=self.request.user)

    def perform_update(self, serializer):
        # prevent non-staff users from making armors public on update
        if not self.request.user.is_staff:
            serializer.save(public=False)
        else:
            serializer.save()