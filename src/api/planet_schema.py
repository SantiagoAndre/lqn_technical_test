import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
#from graphql_jwt.decorators import login_required,user_passes_test

from .models import Planet as PlanetModel


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

  def resolve_planet(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return PlanetModel.objects.get(pk=id)
    return None
  
  def resolve_planets(self, info, *args, **kwargs):
    return PlanetModel.objects.filter(**kwargs)


from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from .forms import CreatePlanetForm

class PlanetMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreatePlanetForm
  
class Mutation(ObjectType):
  planet = PlanetMutation.Field()


