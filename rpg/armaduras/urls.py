from rest_framework.routers import DefaultRouter
from .views import ViewSetArmadura

router = DefaultRouter()
router.register('armaduras', ViewSetArmadura)

urlpatterns = router.urls
