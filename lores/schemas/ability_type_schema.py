from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import AbilityType


class AbilityTypeType(DjangoObjectType):
    class Meta:
        model = AbilityType


class Query(ObjectType):
    ability_type = graphene.Field(AbilityTypeType, id=graphene.Int())
    ability_types = graphene.Field(AbilityTypeType)

    def resolve_ability_type(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return AbilityType.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
