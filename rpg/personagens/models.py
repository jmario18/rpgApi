from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Personagem(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    level = models.IntegerField()
    xp = models.IntegerField(default=0)
    #class1 = models.ForeignKey()
    #class2 = models.ForeignKey()

    def __str__(self):
        return self.nome