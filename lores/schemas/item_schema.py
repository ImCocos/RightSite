from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(ObjectType):
    item = graphene.Field(ItemType, id=graphene.Int())
    items = graphene.Field(ItemType)

    def resolve_item(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Item.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
