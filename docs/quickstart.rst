Quick start guide
=================

Prerequisites
~~~~~~~~~~~~~

* You'll need Django 1.11.1 or later.

* Your project needs to use either Django's default
  :class:`~django.template.backends.django.DjangoTemplates`
  or :class:`~django.template.backends.jinja2.Jinja2`
  template engine.

* Your project needs to use Python 3.

Installation
~~~~~~~~~~~~

.. highlight:: none

This package isn't on PyPI yet, so you'll need to install it directly
from GitHub for now::

    pip install git+git://github.com/18F/django-email-pal

Required settings
~~~~~~~~~~~~~~~~~

Add ``emailpal.apps.EmailPalConfig`` to your ``INSTALLED_APPS`` setting, e.g.:

.. code-block:: python

   INSTALLED_APPS = (
       # ...
       'emailpal.apps.EmailPalConfig',
       # ...
   )
