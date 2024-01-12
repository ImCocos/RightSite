from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Unit


class UnitType(DjangoObjectType):
    class Meta:
        model = Unit


class Query(ObjectType):
    unit = graphene.Field(UnitType, id=graphene.Int())
    units = graphene.Field(UnitType)

    def resolve_unit(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Unit.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
