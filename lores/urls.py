from django.urls import path
from .views import *


urlpatterns = [
    path('stories/', stories, name='stories'),
    path('heroes/', heroes, name='heroes'),
]
