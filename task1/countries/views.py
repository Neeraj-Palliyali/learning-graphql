import requests
import json

from rest_framework import viewsets,serializers
from rest_framework.response import Response

from countries.models import  Language

from .serializers import CountrySaveSerializer, CountrySerializer

# Create your views here.
class CountriesDataSaveViewset(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
   
    def list(self, request, *args, **kwargs):
        call_urll()
        return Response(
            {"success":"True"}
        )

def call_urll():
    response = requests.get("https://restcountries.com/v3.1/all")
    vals = json.loads(response.text)
    for val in vals:
        save_to_db(val)
        
def save_to_db(val):
    try:
        # if the id is a set of strings
        if 'tld' in val:
            val['tld'] = ('_').join(val['tld'])
        
        # If more than one capital for the country
        if 'capital' in val:
            val['capital']= ('_').join(val['capital'])

        serializer = CountrySerializer(data = val)
        
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            valid_data['lat'] = valid_data.get('latlng')[0] 
            valid_data['long'] = valid_data.get('latlng')[1]
            valid_data.pop('latlng')
            save_serializer = CountrySaveSerializer(data= valid_data)
            save_serializer.is_valid(raise_exception=True)
            saved_country = save_serializer.save()
            if 'languages' in val:
                languages = val.get('languages')
                for language in languages.keys(): 
                    Language.objects.create(country = saved_country, 
                                lang_key = language, 
                                language = languages[language])

    except serializers.ValidationError as e:
        print(e)