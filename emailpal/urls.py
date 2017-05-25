from django.conf.urls import url

from emailpal.views import example_view


urlpatterns = [
    url(r'(?P<template_name>.+)\.html', example_view,
        dict(is_html_email=True)),
    url(r'(?P<template_name>.+)\.txt', example_view,
        dict(is_html_email=False)),
]
