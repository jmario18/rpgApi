from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Talento(models.Model):
    TIPOS_TALENTOS =[
        ('origem','Origem'),
        ('geral','Geral'),
        ('épico','Épico')
    ]

    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='talentos', blank=True)
    nome = models.CharField(max_length=35)
    tipo = models.CharField(max_length=10, choices=TIPOS_TALENTOS)
    pre_requisitos = models.CharField(max_length=100, blank=True)
    descricao = models.CharField(max_length=3000)

    def __str__(self):
        return self.nome