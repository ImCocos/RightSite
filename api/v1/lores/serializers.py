from rest_framework import serializers

from lores.models import *
from users.models import *
from api.v1.users.serializers import UserLinkSerializer


class NameSerializer(serializers.Serializer):
    name = serializers.CharField()


class LinkSerializer(serializers.Serializer):
    link = serializers.CharField()


class DescriptionSerializer(serializers.Serializer):
    description = serializers.CharField()


class EffectSerializer(NameSerializer, DescriptionSerializer, LinkSerializer):
    name = serializers.CharField()
    photo = serializers.ImageField()


class UnitSerializer(LinkSerializer, NameSerializer):
    ...


class PerSerializer(serializers.Serializer):
    unit = serializers.CharField()


class AbilityCostSerializer(serializers.Serializer):
    cost = serializers.IntegerField()
    unit = UnitSerializer()
    per = PerSerializer()


class CostSerializer(serializers.Serializer):
    cost = serializers.IntegerField()
    unit = UnitSerializer()


class CategoryLinkSerializer(NameSerializer, LinkSerializer):
    ...


class ItemClassSerializer(NameSerializer, LinkSerializer):
    ...


class AbilityTypeSerializer(serializers.Serializer):
    mode = serializers.CharField()


class AbilitySerializer(NameSerializer, LinkSerializer):
    owner = UserLinkSerializer()
    costs = AbilityCostSerializer(many=True)
    ab_type = AbilityTypeSerializer()
    effects = EffectSerializer(many=True)


class HeroClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroClass
        fields = '__all__'


class ItemSerializer(NameSerializer, LinkSerializer):
    owner = UserLinkSerializer()
    item_class = ItemClassSerializer()
    effects = EffectSerializer(many=True)


class HeroSerializer(NameSerializer, DescriptionSerializer, LinkSerializer):
    id = serializers.IntegerField()
    owner = UserLinkSerializer()
    categories = CategoryLinkSerializer(many=True)
    abilities = AbilitySerializer(many=True)
    items = ItemSerializer(many=True)
    photo = serializers.ImageField()
