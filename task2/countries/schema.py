import graphene
from graphql import GraphQLError
from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType
from graphene_django import DjangoListField
from .models import Country, Language

class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        exclude = ('created_at','updated_at',)
        interfaces = (relay.Node,)

class CoutryConnection(relay.Connection):
    class Meta:
        node = CountryType

class LanguageType(DjangoObjectType):
    class Meta:
        model = Language
        include= '__all__'

class Query(graphene.ObjectType):

    countries_id = graphene.Field(CountryType, id=graphene.Int())
    languages_id = graphene.Field(LanguageType, id=graphene.Int())
    all_countries = DjangoConnectionField(CountryType)

    def resolve_all_countries(self, info,**kwargs):
        return Country.objects.all()

    def resolve_countries_id(self, info, id):
        try:
            val =  Country.objects.get(pk=id)
            return (val)
        except Country.DoesNotExist:
            raise GraphQLError("Country with that ID does not exist") 
            
    def resolve_languages_id(self, info, id):
        return Language.objects.get(pk=id)

schema = graphene.Schema(query=Query)