from rest_framework import viewsets
from django_filters import rest_framework as drf_filters
from logger import logger
from lores import models
from . import serializers


class APIHeroView(viewsets.ModelViewSet):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer
    filter_backends = [drf_filters.DjangoFilterBackend]
    filterset_fields = ['id', 'name']
