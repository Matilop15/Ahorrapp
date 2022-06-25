from django.apps import AppConfig
""" module that defines app config """


class AppConfig(AppConfig):
    """app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
