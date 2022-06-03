from django.apps import AppConfig


class CountriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'countries'

    def ready(self):
        import os
        from .views import call_urll
        if os.environ.get('RUN_MAIN'):
            call_urll()
