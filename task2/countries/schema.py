from itertools import chain
from math import cos, asin, sqrt

import graphene
from graphql import GraphQLError
from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType
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

# query{
#   countriesId(id:4){
#     name,
#           capital,
#           status,
#           independent,
#           region,
#           subregion,
#           capital,
#           lat,
#           long
#   }
# }
    
    languages_id = graphene.Field(LanguageType, id=graphene.Int())
# query{
#   allCountries(first:10){
#     pageInfo {
#         startCursor
#         endCursor
#         hasNextPage
#         hasPreviousPage
#         }
#     edges {
#         cursor
#         node {
#             name,
#           capital
#         }
#     }
#   }
# }
    
    all_countries = DjangoConnectionField(CountryType)
    
# query{
#   closestCoordinate(lat:18.5, long:-63.41666666){
#     name,
#           capital,
#           status,
#           independent,
#           region,
#           subregion,
#           capital,
#           lat,
#           long
#   }
# }
    
    closest_coordinate = graphene.Field(CountryType, lat = graphene.Float(), long = graphene.Float())
    
# query{
#   countryLanguages(language:"English"){
#     name,
#           capital,
#           status,
#           independent,
#           region,
#           subregion,
#           capital,
#           lat,
#           long
#   }
# }
    # country_languages = graphene.List(CountryType, language =  graphene.String())
    country_languages = DjangoConnectionField(CountryType, language =  graphene.String())

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

    def resolve_closest_coordinate(self, info, lat, long):
        try:
            vals = Country.objects.all().values_list('lat', 'long')
            nearest = closest(vals,(lat,long))
            return Country.objects.get(lat = nearest[0], long = nearest[1])
        
        except Country.DoesNotExist:
            raise GraphQLError("No such country exists")

    def resolve_country_languages(self, info, language,**kwargs):
        try:
            languages = Language.objects.filter(language__icontains = language)
            countries = []
            for i in languages:
                country = Country.objects.filter(id = i.id)
                if countries:
                    countries = list(chain(countries, country))
                else:
                    countries = country

            print(countries)
            return countries
        except Exception as e:
            print(e)
    

schema = graphene.Schema(query=Query)


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(data, v):
    return min(data, key=lambda p: distance(v[0],v[1],p[0],p[1]))