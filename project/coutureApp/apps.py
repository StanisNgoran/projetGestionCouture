from django.apps import AppConfig


class CoutureappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coutureApp'

    def ready(self):
        import coutureApp.signals 
