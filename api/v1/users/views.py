from rest_framework import viewsets
from users import models
from . import serializers


class UserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
