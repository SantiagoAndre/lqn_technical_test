import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import superuser_required

from ..models import Productor as ProductorModel



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

  @superuser_required
  def resolve_productor(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return ProductorModel.objects.get(pk=id)
    return None
  @superuser_required
  def resolve_productors(self, info, *args, **kwargs):
    return ProductorModel.objects.filter(**kwargs)


from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from ..forms import CreateProductorForm

class ProductorMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreateProductorForm

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
  productor = ProductorMutation.Field()
