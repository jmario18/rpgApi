from rest_framework.routers import DefaultRouter
from .views import ViewSetArma

router = DefaultRouter()
router.register('armas', ViewSetArma)

urlpatterns = router.urls
