from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
  path('graphql', csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True))),
    name='api.graphql')
]
