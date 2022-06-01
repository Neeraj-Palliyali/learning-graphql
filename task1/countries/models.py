from django.db import models
# Create your models here.
class Country(models.Model):
    tld = models.CharField(max_length=50)
    name = models.CharField( max_length=500)
    status = models.CharField( max_length=100)
    independent = models.BooleanField()
    region = models.CharField( max_length=100)
    subregion = models.CharField( max_length=100)
    capital =  models.CharField( max_length=100)
    lat = models.IntegerField()
    long = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class Language(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    lang_key = models.CharField(max_length=50)
