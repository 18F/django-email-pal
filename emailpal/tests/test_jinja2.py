from pathlib import Path
import pytest


APP_DIR = Path(__file__).resolve().parent.parent
JINJA2_DIR = APP_DIR / 'jinja2' / 'emailpal'
TEMPLATES_DIR = APP_DIR / 'templates' / 'emailpal'


@pytest.mark.parametrize('name', [
    'index.html',
    'really_simple/base.html',
    'really_simple/cta.html',
])
def test_templates_are_identical(name):
    '''
    Some of our templates use the subset of syntax shared by Jinja2 and
    Django Templates, so the two versions of it should be identical.

    Note that this test is currently here to ensure that either
    backend doesn't lag behind the other; however, if a real need
    arises for the templates to diverge, this test shouldn't be
    run on them.
    '''

    parts = name.split('/')
    assert (JINJA2_DIR.joinpath(*parts).read_text() ==
            TEMPLATES_DIR.joinpath(*parts).read_text())
