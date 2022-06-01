import requests
import json

from django.shortcuts import render
from rest_framework import viewsets,serializers
from rest_framework.response import Response

from countries.models import Country

from .serializers import CountrySerializer, LanguageSerializer

# Create your views here.
class CountriesDataSaveViewset(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    # def list(self, request, *args, **kwargs):
        
    #     return super().list(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        response = requests.get("https://restcountries.com/v3.1/all")
        
        vals = json.loads(response.text)
        val = vals[0]
        print(val)
        try:
            if 'tld' in val:
                val['tld'] = ('_').join(val['tld'])
                print(val['tld'])
            serializer = CountrySerializer(data = val)
            
            if serializer.is_valid(raise_exception=True):
                valid_data = serializer.data
                valid_data['lat'] = valid_data['latlng'][0] 
                valid_data['long'] = valid_data['latlng'][1]
                 
                # valid_data.pop('latlng')
        except serializers.ValidationError as e:
            print(e)
            return Response({"success":True})
        return Response(
            {"success":"True"}
        )