from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import ItemClass


class ItemClassType(DjangoObjectType):
    class Meta:
        model = ItemClass


class Query(ObjectType):
    item_class = graphene.Field(ItemClassType, id=graphene.Int())
    item_classes = graphene.Field(ItemClassType)

    def resolve_item_class(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return ItemClass.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
