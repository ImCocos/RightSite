from django.urls import path
from .views import *


urlpatterns = [
    path('user/', user, name='user'),
]
