import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import superuser_required

from .models import Character as CharacterModel


class Character(DjangoObjectType):
  class Meta:
    model = CharacterModel
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith']
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  characters = DjangoFilterConnectionField(Character)
  character = graphene.Field(Character,
                                id=graphene.Int())
  @superuser_required
  def resolve_character(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return CharacterModel.objects.get(pk=id)
    return None
  @superuser_required
  def resolve_characters(self, info, *args, **kwargs):
    return CharacterModel.objects.filter(**kwargs)


from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from .forms import CreateCharacterForm

class CharacterMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreateCharacterForm
  @classmethod
  @superuser_required
  def mutate_and_get_payload(cls, root, info, **input):
    form = cls.get_form(root, info, **input)
    if form.is_valid():
      return cls.perform_mutate(form, info)
    else:
      errors = ErrorType.from_errors(form.errors)
      return cls(errors=errors)
class Mutation(ObjectType):
  character = CharacterMutation.Field()
