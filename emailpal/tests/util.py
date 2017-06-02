from django.conf import settings
from django.test import override_settings


class TemplateSettings(str):
    ENGINE_BACKENDS = {
        'django': 'django.template.backends.django.DjangoTemplates',
        'jinja2': 'django.template.backends.jinja2.Jinja2',
    }

    def enable(self):
        return override_settings(TEMPLATES=[{
            **settings.TEMPLATES[0],
            'BACKEND': self.ENGINE_BACKENDS[self]
        }])


def all_template_engines():
    for name in TemplateSettings.ENGINE_BACKENDS.keys():
        yield TemplateSettings(name)
