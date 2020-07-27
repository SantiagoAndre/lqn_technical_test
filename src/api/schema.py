from graphene import ObjectType, String, Schema
from .character_schema import Query as QueryCharacter,Mutation as MutationCharacter
from .planet_schema import Query as QueryPlanet,Mutation as MutationPlanet


class Query(QueryCharacter,QueryPlanet):
    pass
class Mutation(MutationCharacter,MutationPlanet):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)