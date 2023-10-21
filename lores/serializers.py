from rest_framework import serializers

from .models import *
from users.models import *

from django.core.serializers import serialize


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'link']


class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class PerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Per
        fields = '__all__'


class AbilityCostSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    per = PerSerializer()
    class Meta:
        model = AbilityCost
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
        model = ItemClass
        fields = '__all__'


class AbilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbilityType
        fields = '__all__'


class AbilitySerializer(serializers.ModelSerializer):
    owner = UserLinkSerializer()
    costs = AbilityCostSerializer(many=True)
    ab_type = AbilityTypeSerializer()
    effects = EffectSerializer(many=True)

    class Meta:
        model = Ability
        fields = '__all__'


class HeroClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroClass
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    owner = UserLinkSerializer()
    item_class = ItemClassSerializer()
    effects = EffectSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    owner = UserLinkSerializer()
    categories = CategorySerializer(many=True)
    abilities = AbilitySerializer(many=True)
    items = ItemSerializer(many=True)

    class Meta:
        model = Hero
        fields = '__all__'
