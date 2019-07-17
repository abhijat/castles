from rest_framework.viewsets import ModelViewSet

from castlebuilder.models import Location, Material, Castle
from castlebuilder.serializers import LocationSerializer, MaterialSerializer, CastleSerializer


class LocationsViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class MaterialsViewSet(ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class CastlesViewSet(ModelViewSet):
    serializer_class = CastleSerializer
    queryset = Castle.objects.all()
