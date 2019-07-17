from rest_framework.serializers import ModelSerializer

from castlebuilder.models import Location, Material, Castle


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class CastleSerializer(ModelSerializer):
    class Meta:
        model = Castle
        fields = '__all__'
