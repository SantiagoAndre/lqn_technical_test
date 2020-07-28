import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import superuser_required

from ..models import Movie as MovieModel


class Movie(DjangoObjectType):
  class Meta:
    model = MovieModel
    fields = "__all__"
    filter_fields = {
      'name': ['exact', 'icontains', 'istartswith'],
      'year': ['gt', 'gte', 'lt', 'lte'],
      'director': ['exact', 'icontains', 'istartswith'],
      'opening_crawl': ['exact', 'icontains', 'istartswith'],
      'planets__name': ['exact', 'icontains', 'istartswith'],
      'productors__name': ['exact', 'icontains', 'istartswith']
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  movies = DjangoFilterConnectionField(Movie)
  movie = graphene.Field(Movie,
                                id=graphene.Int())
  @superuser_required
  def resolve_movie(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return MovieModel.objects.get(pk=id)
    return None
  @superuser_required
  def resolve_movies(self, info, *args, **kwargs):
    return MovieModel.objects.filter(**kwargs)


from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from ..forms import CreateMovieForm

class MovieMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreateMovieForm
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
  movie = MovieMutation.Field()
