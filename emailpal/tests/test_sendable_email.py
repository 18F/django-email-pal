import pytest
from mypy_extensions import TypedDict
from django.apps import apps
from django.conf import settings
from django.test import override_settings
from django.core.exceptions import ImproperlyConfigured

from .. import SendableEmail

MyContext = TypedDict('MyContext', {'full_name': str})

class MySendableEmail(SendableEmail[MyContext]):
    template_name = 'my_sendable_email.html'
    subject = 'howdy {full_name}!'


def test_sending_email_works():
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

    e.send_messages(ctx)

    # TODO: Ensure that a message was sent to Django's fake email outbox.


def test_unimportable_sendable_email_raises_import_error():
    with pytest.raises(ImportError):
        with override_settings(SENDABLE_EMAILS=['boop']):
            pass
    # This is weird, but required for the next test to not explode.
    # I think b/c the former exception was raised in a way that "broke"
    # override_settings, preventing it from restoring the old value.
    delattr(settings, 'SENDABLE_EMAILS')


def test_non_sendable_email_raises_improperly_configured_error():
    with pytest.raises(ImproperlyConfigured):
        with override_settings(SENDABLE_EMAILS=['unittest.TestCase']):
            pass
    # This is weird, but required for the next test to not explode.
    # I think b/c the former exception was raised in a way that "broke"
    # override_settings, preventing it from restoring the old value.
    delattr(settings, 'SENDABLE_EMAILS')


@override_settings(SENDABLE_EMAILS=[
    'emailpal.tests.test_sendable_email.MySendableEmail'
])
def test_sendable_email_works():
    cfg = apps.get_app_config('emailpal')
    assert cfg.sendable_emails == [MySendableEmail]
