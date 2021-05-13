from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class ContactConfig(AppConfig):
    name = 'contact'
    def ready(self):
        from . import signals
