Quick start guide
=================

Prerequisites
~~~~~~~~~~~~~

* You'll need Django 1.11.1 or later.

* Your project needs to use either Django's default
  :class:`~django.template.backends.django.DjangoTemplates`
  or :class:`~django.template.backends.jinja2.Jinja2`
  template engine.

* Your project needs to use Python 3.5 or later.

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

Then add the following to your project's ``urls.py``:

.. literalinclude:: ../example/example/urls.py
   :language: python

This sets up the email example gallery at ``/examples/`` on your app. You 
can change it to something else if you want, or you can hide it behind
some logic if you only want it to be exposed during development.

Your first email
~~~~~~~~~~~~~~~~

Let's get started by adding an email example to your project. We're
going to assume that your project has an app called ``example`` in it.

Create a file at ``example\emails.py`` and put the following in it:

.. literalinclude:: ../example/example/emails.py
   :language: python

Then create a file at ``example\templates\example\my_template.html`` and
put this in it:

.. literalinclude:: ../example/example/templates/example/my_template.html
   :language: html+django

As you can probably guess, the email expects the context variable
``full_name`` to contain the full name of the recipient. The example
version of the email will use "Jane Doe".

The email will also contain a call-to-action (CTA) that directs the
user to a website.

Now we just need to let the email example gallery know about the
existence of your new template. Do this by adding the following to
your project's ``settings.py``:

.. literalinclude:: ../example/example/settings.py
   :language: python
   :start-after: Start SENDABLE_EMAILS doc snippet
   :end-before: End SENDABLE_EMAILS doc snippet

Now you're set! Start your app and visit ``/examples/``; you should
see the email gallery with a single entry, and be able to view your
example email as HTML and plaintext.
