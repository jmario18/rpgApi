from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    TIPO_ITEM = [
        ('pocao', 'Poção'),
        ('anel', 'Anel'),
        ('cajado','Cajado'),
        ('varinha', 'Varinha'),
        ('item maravilhoso', 'Item Maravilhoso')
    ]

    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itens', blank=True)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_ITEM)
    sintonizacao = models.BooleanField(default=False)
    #class = models.ForeignKey
    descricao = models.CharField(max_length=10000)

    def __str__(self):
        return self.nome