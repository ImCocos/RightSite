from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logger import logger
from lores.models import *
from .serializers import *


class APIHeroView(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
