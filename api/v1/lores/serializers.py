from rest_framework import serializers

from lores import models as lores_models
from api.v1.users import serializers as api_v1_users_serializers


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
    owner = api_v1_users_serializers.UserLinkSerializer()
    costs = AbilityCostSerializer(many=True)
    ab_type = AbilityTypeSerializer()
    effects = EffectSerializer(many=True)


class HeroClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = lores_models.HeroClass
        fields = '__all__'


class ItemSerializer(NameSerializer, LinkSerializer):
    owner = api_v1_users_serializers.UserLinkSerializer()
    item_class = ItemClassSerializer()
    effects = EffectSerializer(many=True)


class HeroSerializer(NameSerializer, DescriptionSerializer, LinkSerializer):
    id = serializers.IntegerField()
    owner = api_v1_users_serializers.UserLinkSerializer()
    categories = CategoryLinkSerializer(many=True)
    abilities = AbilitySerializer(many=True)
    items = ItemSerializer(many=True)
    photo = serializers.ImageField()
