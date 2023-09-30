from django.urls import path
from .views import *


urlpatterns = [
    path('heroes/', heroes, name='heroes'),
]
