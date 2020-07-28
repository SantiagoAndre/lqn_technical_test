import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import superuser_required

from ..models import Planet as PlanetModel


class Planet(DjangoObjectType):
  class Meta:
    model = PlanetModel
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith']
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  planets = DjangoFilterConnectionField(Planet)
  planet = graphene.Field(Planet,
                                id=graphene.Int())
  @superuser_required
  def resolve_planet(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return PlanetModel.objects.get(pk=id)
    return None
  @superuser_required
  def resolve_planets(self, info, *args, **kwargs):
    return PlanetModel.objects.filter(**kwargs)


from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from ..forms import CreatePlanetForm

class PlanetMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreatePlanetForm
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
  planet = PlanetMutation.Field()


