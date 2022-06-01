from django.contrib import admin

from .models import Country, Language

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)

admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)