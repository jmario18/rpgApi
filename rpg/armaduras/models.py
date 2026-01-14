from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Armadura(models.Model):
    TIPOS_ARMADURA = [
        ('leve', 'Leve,'),
        ('média', 'Média'),
        ('pesada', 'Pesada')
    ]

    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='armaduras')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS_ARMADURA)
    classeDeArmadura = models.PositiveIntegerField()
    peso = models.FloatField(null=True, blank=True)
    extra = models.CharField(blank=True, max_length=5000)


    def __str__(self):
        return self.nome