from django.apps import AppConfig


class CosplayappConfig(AppConfig):
    name = 'cosplayapp'

    def ready(self):
        import cosplayapp.signals

