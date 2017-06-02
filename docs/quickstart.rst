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

.. important::

    If you're using Jinja2, you'll want to put the template at
    ``example\jinja2\example\my_template.html``.

    Also, replace the line containing the ``{% include %}`` directive
    with the following:

    .. literalinclude:: ../example/example/jinja2/example/my_template.html
       :language: html+django
       :start-after: Start jinja2 doc snippet
       :end-before: End jinja2 doc snippet

As you can probably guess, the email expects the context variable
``full_name`` to contain the full name of the recipient. The example
version of the email will use "Jane Doe".

The email will also contain a call-to-action (CTA) that directs the
user to a website.

Registering the email with the gallery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Sending the email
~~~~~~~~~~~~~~~~~

You can create a Django :py:class:`~django.core.mail.EmailMessage` with your
email's :py:meth:`~emailpal.SendableEmail.create_message` method like so:

.. literalinclude:: ../emailpal/tests/test_sendable_email.py
   :language: python
   :dedent: 4
   :start-after: Start create_message doc snippet
   :end-before: End create_message doc snippet

Then you can send the message with ``msg.send()``.

Adding smoke tests
~~~~~~~~~~~~~~~~~~

Since your email has an example context, it's straightforward
to add smoke tests for it: just render the email with the
example context and make sure nothing explodes. In fact, 
django-email-pal comes with tooling that makes this
particularly easy.

Just create a new test module and add the following
to it:

.. literalinclude:: ../example/example/tests/test_emails_do_not_smoke.py
   :language: python

Now when you run ``manage.py test`` (or whatever your
choice of test runners is), all the emails you've listed
in ``settings.SENDABLE_EMAILS`` will be rendered with their
example context to ensure that they don't throw any exceptions.
