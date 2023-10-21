import graphene
import lores.schemas.hero_schema


class Query(lores.schemas.hero_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

'''
class Mutation(lores.schemas.hero_schema, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
'''
schema = graphene.Schema(query=Query)
