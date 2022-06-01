from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CountriesDataSaveViewset

router = DefaultRouter(trailing_slash = False)

router.register(r'show_countries', CountriesDataSaveViewset, basename= 'countries')

urlpatterns = [
    path("api/", include(router.urls))
]

