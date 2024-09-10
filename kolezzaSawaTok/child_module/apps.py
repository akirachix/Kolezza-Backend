from django.apps import AppConfig


class ChildModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'child_module'
