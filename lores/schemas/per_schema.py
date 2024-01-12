from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Per


class PerType(DjangoObjectType):
    class Meta:
        model = Per


class Query(ObjectType):
    per = graphene.Field(PerType, id=graphene.Int())
    pers = graphene.Field(PerType)

    def resolve_per(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Per.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
