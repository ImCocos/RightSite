from rest_framework import serializers

from users.models import *


class UserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'link']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'link', 'email']
