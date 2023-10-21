from django.shortcuts import render

from logger import logger
from .models import *
from .apps import LoresConfig


app_name = LoresConfig.name


def heroes(request):
    return render(request, template_name=f'{app_name}/heroes.html')
