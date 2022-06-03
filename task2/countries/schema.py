import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Country, Language


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        exclude = ('created_at','updated_at')

class LanguageType(DjangoObjectType):
    class Meta:
        model = Language
        exclude = ('created_at','updated_at')

class Query(graphene.ObjectType):

    countries_id = graphene.Field(CountryType, id=graphene.Int())
    languages_id = graphene.List(LanguageType, id=graphene.Int())

    def resolve_countries_id(root, info, id):
        return Country.objects.get(pk=id)
    def resolve_languages_id(root, info, id):
        return Language.objects.filter(pk=id)

schema = graphene.Schema(query=Query)