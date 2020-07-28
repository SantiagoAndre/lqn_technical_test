import json
from django.contrib.auth import get_user_model

from graphene_django.utils.testing import GraphQLTestCase
from .schema import    ROOT_SCHEMA as schema

class MutationssTestCase(GraphQLTestCase):
     # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema
    def test_login(self):
        username = "test"
        password = "test"
        get_user_model().objects.create(is_superuser=True,username=username,password=password)
        response = self.query(
            '''
            mutation tokenAuth($input: MyMutationInput!) {
                tokenAuth(input: $input) {
                    my-model {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='tokenAuth',
            input_data={'password': password, 'username': username}
        )
        print(response.content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

    def test_some_query(self):
        response = self.query(
            '''
            query {
                characters(name_Icontains:"1"){
                    edges{
                    node{
                        id
                        name
                    }
                    }
                }
                character(id:1){
                    id
                    name
                }
                planets(name_Icontains:"232"){
                    edges{
                    node{
                        id
                        name
                    }
                    }
                }
                planet(id:2){
                    id
                    name
                }
                    productors(name_Icontains:"s"){
                    edges{
                    node{
                        id
                        name
                    }
                    }
                }
                productor(id:2){
                    id
                    name
                }
                    movies(productors_Name_Icontains:"1"){
                    edges{
                    node{
                        id
                        name
                        productors{
                        edges{
                            node{
                            name
                            }
                        }
                        }
                    }
                    }
                }
                productor(id:2){
                    id
                    name
                }
            }
            ''',
            op_name='query'
        )
        print(response.content)
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)



