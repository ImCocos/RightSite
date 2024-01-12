from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import AbilityCost


class AbilityCostType(DjangoObjectType):
    class Meta:
        model = AbilityCost


class Query(ObjectType):
    ability_cost = graphene.Field(AbilityCostType, id=graphene.Int())
    ability_costs = graphene.Field(AbilityCostType)

    def resolve_ability_cost(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return AbilityCost.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
