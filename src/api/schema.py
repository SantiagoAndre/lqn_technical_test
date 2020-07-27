from graphene import ObjectType, String, Schema
from .character_schema import Query as QueryCharacter,Mutation as MutationCharacter


class Query(QueryCharacter):
    pass
class Mutation(MutationCharacter):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)