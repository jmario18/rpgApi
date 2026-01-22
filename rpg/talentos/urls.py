from rest_framework.routers import DefaultRouter
from .views import ViewSetTalento

router = DefaultRouter()
router.register('talentos', ViewSetTalento)

urlpatterns = router.urls
