from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class Query(ObjectType):
    hero = graphene.Field(HeroType, id=graphene.Int())
    heros = graphene.Field(HeroType)

    def resolve_hero(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Hero.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
