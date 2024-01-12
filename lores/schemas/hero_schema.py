from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Hero
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

class HeroType(DjangoObjectType):
    class Meta:
        model = Hero
        filter_fields = {
            'name': ['exact', 'in', 'icontains'],
            'id': ['exact', 'in', 'icontains'],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    hero = graphene.Field(
        HeroType,
        id=graphene.ID(),
        name=graphene.String())
    heros = DjangoFilterConnectionField(HeroType)

    def resolve_hero(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Hero.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
