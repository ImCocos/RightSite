from rest_framework import serializers

from users import models as user_models


class UserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ['username', 'link']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ['pk', 'username', 'link', 'email']
