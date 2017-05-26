from typing import List  # NOQA
from django.apps import AppConfig
from django.conf import settings
from django.utils.module_loading import import_string
from django.core.exceptions import ImproperlyConfigured
from django.core.signals import setting_changed

from .sendable_email import SendableEmail


class EmailPalConfig(AppConfig):
    name = 'emailpal'
    verbose_name = 'Email Pal'

    sendable_emails = []  # type: List[SendableEmail]

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
