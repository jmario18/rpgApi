from django.contrib import admin
from .models import Personagem, PersonagemArma, PersonagemArmadura

# Register your models here.

# criar inlines para depois criar a classe Admin
class PersonagemArmaInline(admin.TabularInline):
    model = PersonagemArma

class PersonagemArmaduraInline(admin.TabularInline):
    model = PersonagemArmadura

# fazer isso faz com que PersonagemArma e PersonagemArmadura seja modificado diretamentedo personagem
@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    inlines = [PersonagemArmaInline, PersonagemArmaduraInline]

