from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Ability


class AbilityType(DjangoObjectType):
    class Meta:
        model = Ability


class Query(ObjectType):
    ability = graphene.Field(AbilityType, id=graphene.Int())
    abilities = graphene.Field(AbilityType)

    def resolve_ability(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ability.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
