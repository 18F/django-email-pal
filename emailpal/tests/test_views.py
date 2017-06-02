import pytest
from django.conf.urls import include, url
from django.test import Client, override_settings

from .util import all_template_engines
from .test_sendable_email import MY_SENDABLE_EMAIL

urlpatterns = [
    url(r'^examples/', include('emailpal.urls')),
]

@pytest.fixture
def client():
    with override_settings(SENDABLE_EMAILS=[MY_SENDABLE_EMAIL],
                           ROOT_URLCONF=__name__):
        yield Client()


@pytest.mark.parametrize('template_engine', all_template_engines())
def test_index_works(client, template_engine):
    with template_engine.enable():
        response = client.get('/examples/')
        assert response.status_code == 200
        assert 'MySendableEmail' in response.content.decode('utf-8')


def test_invalid_example_raises_404(client):
    response = client.get('/examples/blarg.html')
    assert response.status_code == 404


def test_valid_html_example_works(client):
    response = client.get('/examples/{}.html'.format(MY_SENDABLE_EMAIL))
    assert response.status_code == 200
    assert 'I am HTML' in response.content.decode('utf-8')


def test_valid_plaintext_example_works(client):
    response = client.get('/examples/{}.txt'.format(MY_SENDABLE_EMAIL))
    assert response.status_code == 200
    assert 'I am plaintext' in response.content.decode('utf-8')
