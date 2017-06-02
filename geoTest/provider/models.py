from django.contrib.gis.db import models
from django.utils import timezone


class Provider(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    poly = models.PolygonField(null=True, blank=True)
    price = models.FloatField(default=0.0)
    currency = models.CharField(max_length=50, default='$')
    reg_date = models.DateTimeField(default=timezone.now)
    provider = models.ForeignKey(Provider)

    def __str__(self):
        return self.name
