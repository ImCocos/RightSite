from rest_framework import serializers
from .models import *
from django.core.serializers import serialize


class PageObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageObject
        fields = '__all__'


class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Cost
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AbilitySerializer(serializers.ModelSerializer):
    costs = CostSerializer(many=True)
    class Meta:
        model = Ability
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    item_class = ItemClassSerializer()
    effects = EffectSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    page_objects = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'
    
    def get_page_objects(self, obj):
        return [PageObjectSerializer(PageObject.objects.get(pk=i)).data for i in obj.page_objects]


class HeroSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    abilities = AbilitySerializer(many=True)
    items = ItemSerializer(many=True)


    class Meta:
        model = Hero
        fields = '__all__'

