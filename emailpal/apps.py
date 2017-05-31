from typing import List, Type  # NOQA
from collections import OrderedDict
from django.apps import AppConfig, apps
from django.conf import settings
from django.utils.module_loading import import_string
from django.core.exceptions import ImproperlyConfigured
from django.core.signals import setting_changed

from .sendable_email import SendableEmail


class EmailPalConfig(AppConfig):
    name = 'emailpal'
    verbose_name = 'Email Pal'

    sendable_emails = []  # type: List[Type[SendableEmail]]

    def get_sendable_emails(self) -> OrderedDict:
        result = OrderedDict()  # type: OrderedDict[str, Type[SendableEmail]]
        names = getattr(settings, 'SENDABLE_EMAILS', [])
        for name, sendable_email_cls in zip(names, self.sendable_emails):
            result[name] = sendable_email_cls
        return result

    def configure_sendable_emails(self):
        self.sendable_emails[:] = []
        for name in getattr(settings, 'SENDABLE_EMAILS', []):
            cls = import_string(name)
            if not issubclass(cls, SendableEmail):
                raise ImproperlyConfigured(
                    '{} must be a subclass of SendableEmail'.format(name)
                )
            self.sendable_emails.append(cls)

    def _on_setting_changed(self, setting=None, enter=None, **kwargs):
        if setting == 'SENDABLE_EMAILS':
            self.configure_sendable_emails()

    def ready(self):
        self.configure_sendable_emails()
        setting_changed.connect(self._on_setting_changed)


def get_sendable_emails() -> OrderedDict:
    return apps.get_app_config('emailpal').get_sendable_emails()
