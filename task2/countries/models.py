from django.db import models
# Create your models here.
class Country(models.Model):
    tld = models.CharField(blank=True, max_length=50)
    name = models.CharField( max_length=500)
    status = models.CharField( max_length=100)
    independent = models.BooleanField()
    region = models.CharField( max_length=100)
    subregion = models.CharField( blank=True,max_length=100)
    capital =  models.CharField(blank=True, max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    lang_key = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.country.name
