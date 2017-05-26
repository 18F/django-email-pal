from pathlib import Path

MY_DIR = Path(__file__).parent.resolve()
APP_DIR = MY_DIR.parent

# Minimum settings required for the app's tests.
SETTINGS_DICT = {
    'BASE_DIR': str(APP_DIR),
    'INSTALLED_APPS': (
        'emailpal.apps.EmailPalConfig',
    ),
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(APP_DIR / 'db.sqlite3'),
        },
    },
    'MIDDLEWARE_CLASSES': (
        'django.middleware.common.CommonMiddleware',
    ),
    'TEMPLATES': [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(MY_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    }],
}


def init_django():
    # Making Django run this way is a two-step process. First, call
    # settings.configure() to give Django settings to work with:
    from django.conf import settings
    settings.configure(**SETTINGS_DICT)

    # Then, call django.setup() to initialize the application cache
    # and other bits:
    import django
    django.setup()


# Originally we defined this as a session-scoped fixture, but that
# broke django.test.SimpleTestCase instances' class setup methods,
# so we need to call this function *really* early.
init_django()
