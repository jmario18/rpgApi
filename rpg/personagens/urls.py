from rest_framework.routers import DefaultRouter
from .views import ViewSetPersonagem, ViewSetPersonagemArma, ViewSetPersonagemArmadura

router = DefaultRouter()
router.register('personagens', ViewSetPersonagem, basename='personagens')
router.register('personagem-armas', ViewSetPersonagemArma, basename='personagem-armas')
router.register('personagem-armadura', ViewSetPersonagemArmadura, basename='personagem-armadura')
urlpatterns = router.urls
