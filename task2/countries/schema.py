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

    # Get country by ID
    countries_id = graphene.Field(CountryType, id=graphene.Int())

    # Paginated Countries
    all_countries = DjangoConnectionField(CountryType)
    
    # Closest country to the given co-ordinates
    closest_coordinate = graphene.Field(CountryType, lat = graphene.Float(), long = graphene.Float())
    
    # paginated countries with specific language
    country_languages = DjangoConnectionField(CountryType, language =  graphene.String())

    # Function to get all countries paginated
    def resolve_all_countries(self, info,**kwargs):
        return Country.objects.all()

    # Get country based on the ID
    def resolve_countries_id(self, info, id):
        try:
            return Country.objects.get(pk=id)

        # Rasing exception if country does not exists
        except Country.DoesNotExist:
            raise GraphQLError("Country with that ID does not exist") 
    
    # Get the closest country with the co-ordinates given
    def resolve_closest_coordinate(self, info, lat, long):
        try:
            vals = Country.objects.all().values_list('lat', 'long')
            nearest = closest(vals,(lat,long))
            return Country.objects.get(lat = nearest[0], long = nearest[1])
        
        except Country.DoesNotExist:
            raise GraphQLError("No such country exists")
    
    #Getting the countries with the specific language spoken 
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
            return countries
        except Language.DoesNotExist:
            raise GraphQLError("Such a Language does not exist")
    
        except Country.DoesNotExist:
            raise GraphQLError("Such a Country does not exist")

schema = graphene.Schema(query=Query)


# UTILS functions to get the closest distance
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(data, v):
    return min(data, key=lambda p: distance(v[0],v[1],p[0],p[1]))