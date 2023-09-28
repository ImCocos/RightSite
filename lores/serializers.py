from rest_framework import serializers
from .models import *
from django.core.serializers import serialize


class PageObjectSerializer(serializers.ModelSerializer):
    """
    the serializator that returns json data with all fields
    """
    class Meta:
        model = PageObject
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    page_objects = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'
    
    def get_page_objects(self, obj):
        return [PageObjectSerializer(PageObject.objects.get(pk=i)).data for i in obj.page_objects]


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

