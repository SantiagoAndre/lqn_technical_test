import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
#from graphql_jwt.decorators import login_required,user_passes_test

from .models import Productor as ProductorModel


class Productor(DjangoObjectType):
  class Meta:
    model = ProductorModel
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith']
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  productors = DjangoFilterConnectionField(Productor)
  productor = graphene.Field(Productor,
                                id=graphene.Int())

  def resolve_productor(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return ProductorModel.objects.get(pk=id)
    return None
  
  def resolve_productors(self, info, *args, **kwargs):
    return ProductorModel.objects.filter(**kwargs)


from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from .forms import CreateProductorForm

class ProductorMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreateProductorForm
  
class Mutation(ObjectType):
  productor = ProductorMutation.Field()
