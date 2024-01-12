from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Effect


class EffectType(DjangoObjectType):
    class Meta:
        model = Effect


class Query(ObjectType):
    effect = graphene.Field(EffectType, id=graphene.Int())
    effects = graphene.Field(EffectType)

    def resolve_effect(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Effect.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
