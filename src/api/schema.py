from graphene import ObjectType, String, Schema
from .character_schema import Query as QueryCharacter,Mutation as MutationCharacter
from .planet_schema import Query as QueryPlanet,Mutation as MutationPlanet
from .productor_schema import Query as QueryProductor,Mutation as MutationProductor


class Query(QueryCharacter,QueryPlanet,QueryProductor):
    pass
class Mutation(MutationCharacter,MutationPlanet,MutationProductor):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)