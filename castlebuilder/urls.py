from rest_framework.routers import DefaultRouter

from castlebuilder.views import CastlesViewSet, MaterialsViewSet, LocationsViewSet

router = DefaultRouter()
router.register('castles', CastlesViewSet)
router.register('materials', MaterialsViewSet)
router.register('locations', LocationsViewSet)

urlpatterns = router.urls
