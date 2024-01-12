from graphene_django.types import DjangoObjectType, ObjectType
import graphene

from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.Field(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return User.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
