from django.test import TestCase
from emailpal.tests.util import all_template_engines

from ..emails import MySendableEmail


class RenderingParityTests(TestCase):
    def test_email_renders_the_same_in_all_engines(self):
        e = MySendableEmail()
        engine_output = {}
        for engine in all_template_engines():
            out = {}  # type: dict
            engine_output[engine] = out
            with engine.enable():
                out['txt'] = e.render_body_as_plaintext(e.example_ctx)
                out['html'] = e.render_body_as_html(e.example_ctx)
        self.maxDiff = 5000
        self.assertEqual(
            engine_output['django']['txt'],
            engine_output['jinja2']['txt'],
        )
        self.assertHTMLEqual(
            engine_output['django']['html'],
            engine_output['jinja2']['html'],
        )
