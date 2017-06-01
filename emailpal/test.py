"""
    This module is meant to provide utilities that make it
    easy for Django projects using django-email-pal to
    test their emails.

    For the test suite which tests django-email-pal itself,
    see the tests/ directory.
"""

from unittest import SkipTest

from .apps import get_sendable_emails


class EmailSmokeTestsMixin:
    def subtest_emails(self):
        emails = get_sendable_emails()
        if len(emails) == 0:
            raise SkipTest('no emails to test')
        for name, email_class in emails.items():
            with self.subTest(email_class=name):
                yield email_class()

    def test_emails_render_body_as_html(self):
        for email in self.subtest_emails():
            email.render_body_as_html(email.example_ctx)

    def test_emails_render_body_as_plaintext(self):
        for email in self.subtest_emails():
            email.render_body_as_plaintext(email.example_ctx)

    def test_emails_render_subject(self):
        for email in self.subtest_emails():
            email.render_subject(email.example_ctx)
