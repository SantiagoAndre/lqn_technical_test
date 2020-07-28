from graphene import ObjectType, String, Schema
from .schemas.character_schema import Query as QueryCharacter,Mutation as MutationCharacter
from .schemas.planet_schema import Query as QueryPlanet,Mutation as MutationPlanet
from .schemas.productor_schema import Query as QueryProductor,Mutation as MutationProductor
from .schemas.movie_schema import Query as QueryMovie,Mutation as MutationMovie
from .schemas.auth_schema import Mutation as AuthMutation


class Query(QueryCharacter,QueryPlanet,QueryProductor,QueryMovie):
    pass
class Mutation(AuthMutation,MutationCharacter,MutationPlanet,MutationProductor,MutationMovie):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)