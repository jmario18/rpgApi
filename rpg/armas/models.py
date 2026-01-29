from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Arma(models.Model):
    DADOS_DANOS = [
        ('d4','d4'),
        ('d6','d6'),
        ('d8','d8'),
        ('d10','d10'),
        ('d12','d12'),
    ]

    TIPO_ARMA = [
        ('simples', 'Simples'),
        ('marcial', 'Marcial')
    ]

    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='armas', blank=True)
    public = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)
    tipo = models.CharField(default='Simples',max_length=7, choices=TIPO_ARMA)
    n_dado = models.IntegerField(default=1)
    dano = models.CharField(max_length=3, choices=DADOS_DANOS)
    n_dado_ex = models.IntegerField(default=0, blank=True)
    dano_ex = models.CharField(max_length=3, choices=DADOS_DANOS, blank=True)
    efeitos_extras = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return self.nome