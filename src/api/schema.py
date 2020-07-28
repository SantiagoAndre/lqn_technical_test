from graphene import ObjectType, String, Schema
from .character_schema import Query as QueryCharacter,Mutation as MutationCharacter
from .planet_schema import Query as QueryPlanet,Mutation as MutationPlanet
from .productor_schema import Query as QueryProductor,Mutation as MutationProductor
from .movie_schema import Query as QueryMovie,Mutation as MutationMovie
from .auth_schema import Mutation as AuthMutation


class Query(QueryCharacter,QueryPlanet,QueryProductor,QueryMovie):
    pass
class Mutation(AuthMutation,MutationCharacter,MutationPlanet,MutationProductor,MutationMovie):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)