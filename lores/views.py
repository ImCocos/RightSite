from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .apps import LoresConfig
from .serializers import *


app_name = LoresConfig.name


class APIHeroView(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']

def heroes(request):
    return render(request, template_name=f'{app_name}/heroes.html')
