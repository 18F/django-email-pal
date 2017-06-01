import pytest
from collections import OrderedDict
from mypy_extensions import TypedDict
from django.apps import apps as django_apps
from django.conf import settings
from django.core import mail
from django.test import override_settings
from django.core.exceptions import ImproperlyConfigured

from .. import SendableEmail, apps

MyContext = TypedDict('MyContext', {'full_name': str})

class MySendableEmail(SendableEmail[MyContext]):
    example_ctx = {'full_name': 'foo bar'}
    template_name = 'my_sendable_email.html'
    subject = 'howdy {full_name}!'


MY_SENDABLE_EMAIL = '{}.{}'.format(__name__, MySendableEmail.__name__)


def test_rendering_email_works():
    ctx = MyContext(full_name='boop jones')
    e = MySendableEmail()

    assert e.render_subject(ctx) == 'howdy boop jones!'

    html = e.render_body_as_html(ctx)
    text = e.render_body_as_plaintext(ctx)

    assert "Hello boop jones" in html
    assert "Hello boop jones" in text

    assert "I am plaintext" in text
    assert "I am not HTML" in text

    assert "I am HTML" in html
    assert "I am <strong>not</strong> plaintext" in html


@pytest.fixture
def mail_connection():
    mail.outbox = []
    with mail.get_connection() as connection:
        yield connection


def test_email_sending_works(mail_connection):
    # Start create_message doc snippet
    msg = MySendableEmail().create_message(
        {'full_name': 'boop jones'},
        from_email='foo@example.org',
        to=['bar@example.org'],
        headers={'Message-ID': 'blah'},
    )
    # End create_message doc snippet

    msg.connection = mail_connection
    num_sent = msg.send(fail_silently=False)
    assert num_sent == 1
    assert len(mail.outbox) == 1
    msg = mail.outbox[0]
    assert msg.subject == 'howdy boop jones!'
    assert 'I am plaintext' in msg.body
    assert len(msg.alternatives) == 1
    alt = msg.alternatives[0]
    assert 'I am HTML' in alt[0]
    assert alt[1] == 'text/html'


def test_error_raised_if_ctx_is_not_a_dict():
    with pytest.raises(ValueError) as excinfo:
        MySendableEmail()._cast_to_dict(1)  # type: ignore
    assert 'must be a dict subclass' in str(excinfo)


def test_unimportable_sendable_email_raises_import_error():
    with pytest.raises(ImportError):
        with override_settings(SENDABLE_EMAILS=['boop']):
            pass  # pragma: no cover
    # This is weird, but required for the next test to not explode.
    # I think b/c the former exception was raised in a way that "broke"
    # override_settings, preventing it from restoring the old value.
    delattr(settings, 'SENDABLE_EMAILS')


def test_non_sendable_email_raises_improperly_configured_error():
    with pytest.raises(ImproperlyConfigured):
        with override_settings(SENDABLE_EMAILS=['unittest.TestCase']):
            pass  # pragma: no cover
    # This is weird, but required for the next test to not explode.
    # I think b/c the former exception was raised in a way that "broke"
    # override_settings, preventing it from restoring the old value.
    delattr(settings, 'SENDABLE_EMAILS')


@override_settings(SENDABLE_EMAILS=[MY_SENDABLE_EMAIL])
def test_sendable_email_works():
    cfg = django_apps.get_app_config('emailpal')
    assert cfg.sendable_emails == [MySendableEmail]


@override_settings(SENDABLE_EMAILS=[MY_SENDABLE_EMAIL])
def test_get_sendable_emails_works():
    assert apps.get_sendable_emails() == OrderedDict([
        ('emailpal.tests.test_sendable_email.MySendableEmail',
         MySendableEmail)
    ])
