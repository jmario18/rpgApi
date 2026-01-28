from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from armas.models import Arma
from armaduras.models import Armadura

# Create your models here.

class Personagem(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    level = models.IntegerField()
    xp = models.IntegerField(default=0)
    # Classes app needed
    #class1 = models.ForeignKey()
    #class2 = models.ForeignKey()
    backstory = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.nome
    
class PersonagemArma(models.Model):

    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE,related_name="armas")
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE, related_name="donos")

    quantidade = models.PositiveIntegerField(default=0)
    equipado = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.personagem} - {self.arma} ({self.quantidade})"
    
class PersonagemArmadura(models.Model):
    
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, related_name="armaduras")
    armadura = models.ForeignKey(Armadura, on_delete=models.CASCADE, related_name="donos")

    equipado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.personagem} - {self.armadura}"