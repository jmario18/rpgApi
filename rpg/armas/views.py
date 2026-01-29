from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Arma
from .serializers import SerializerArma
from .permissions import EhDonoOuAdmin


# Create your views here.

class ViewSetArma(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = SerializerArma
    permission_classes = [permissions.IsAuthenticated, EhDonoOuAdmin]

    def get_queryset(self):
        # return armas owned by the user or marked as public
        return Arma.objects.filter(Q(dono=self.request.user) | Q(public=True))
    
    def perform_create(self, serializer):
        # prevent non-staff users from creating public weapons
        if not self.request.user.is_staff:
            serializer.save(dono=self.request.user, public=False)
        else:
            serializer.save(dono=self.request.user)

    def perform_update(self, serializer):
        # prevent non-staff users from making weapons public on update
        if not self.request.user.is_staff:
            serializer.save(public=False)
        else:
            serializer.save()