from django.db import models


class Castle(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, unique=True)

    budget = models.FloatField(null=False, blank=False)

    material = models.ForeignKey(to='Material', related_name='castles', on_delete=models.deletion.DO_NOTHING)
    location = models.ForeignKey(to='Location', related_name='castles', on_delete=models.deletion.DO_NOTHING)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Material(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, unique=True)

    weight_per_ton = models.FloatField(null=False, blank=False)
    flammable = models.BooleanField(default=False)

    mined_at = models.ForeignKey('Location', related_name='materials', on_delete=models.deletion.DO_NOTHING)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Location(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False, unique=True)

    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
