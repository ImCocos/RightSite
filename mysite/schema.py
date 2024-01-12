import graphene
from lores.schemas.all import all_schemas as lores_queries
from users.schemas.all import all_schemas as users_queries


class Query(
    *lores_queries,
    *users_queries,
    graphene.ObjectType,
): ...


schema = graphene.Schema(query=Query)
