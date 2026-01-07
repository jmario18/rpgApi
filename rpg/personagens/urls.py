from rest_framework.routers import DefaultRouter
from .views import ViewSetPersonagem

router = DefaultRouter()
router.register('personagens', ViewSetPersonagem)

urlpatterns = router.urls
