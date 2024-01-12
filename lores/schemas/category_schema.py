from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from lores.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(ObjectType):
    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.Field(CategoryType)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Category.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
