from rest_framework.routers import DefaultRouter
from .views import ViewSetItem

router = DefaultRouter()
router.register('itens', ViewSetItem)

urlpatterns = router.urls
