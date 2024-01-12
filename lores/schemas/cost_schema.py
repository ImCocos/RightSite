from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Cost


class CostType(DjangoObjectType):
    class Meta:
        model = Cost


class Query(ObjectType):
    cost = graphene.Field(CostType, id=graphene.Int())
    costs = graphene.Field(CostType)

    def resolve_cost(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Cost.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
