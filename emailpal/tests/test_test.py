from unittest import TestCase, SkipTest
import pytest
from django.test import override_settings

from .test_sendable_email import MY_SENDABLE_EMAIL
from emailpal.test import EmailSmokeTestsMixin


@override_settings(SENDABLE_EMAILS=[MY_SENDABLE_EMAIL])
def test_smoke_tests_are_run_on_sendable_emails():
    class MyTests(TestCase, EmailSmokeTestsMixin):
        pass

    for name in ['test_emails_render_body_as_html',
                 'test_emails_render_body_as_plaintext',
                 'test_emails_render_subject']:
        result = MyTests(name).run()
        assert result.errors == []     # type: ignore
        assert result.failures == []   # type: ignore
        assert result.skipped == []    # type: ignore
        assert result.testsRun == 1    # type: ignore
        assert result.wasSuccessful()  # type: ignore


@override_settings(SENDABLE_EMAILS=[])
def test_smoke_tests_raise_skiptest_if_no_emails_are_found():
    class MyTests(TestCase, EmailSmokeTestsMixin):
        pass

    with pytest.raises(SkipTest):
        MyTests().subtest_emails().__next__()
