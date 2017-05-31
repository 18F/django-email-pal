from django.conf.urls import url

from emailpal.views import example_view, example_index

app_name = 'emailpal'

urlpatterns = [
    url(r'^$', example_index, name='index'),
    url(r'^(?P<name>.+)\.html$', example_view,
        dict(is_html_email=True), name='example_view_html'),
    url(r'^(?P<name>.+)\.txt$', example_view,
        dict(is_html_email=False), name='example_view_txt'),
]
