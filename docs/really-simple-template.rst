Really simple template
======================

This package comes with an optional template based on Lee Munroe's
`Really Simple Responsive HTML Email Template`_ that makes it
easy to get started with sending HTML emails that look nice.

For an example of this template in use, see :ref:`Your first email`.

Base template
-------------

Emails can use the base template by extending
``emailpal/really_simple/base.html``.

Variables used
::::::::::::::

This template has no special variables aside from the ones you
include in your context and the ones defined by
:py:class:`emailpal.SendableEmail`.

Blocks defined
::::::::::::::

These can be overridden by templates that inherit from the base. Unless
otherwise stated, all blocks default to empty content.

``content``
    The content for the email.
``preheader``
    The contents of a ``<span>`` with a ``class`` of ``preheader``, which some email clients will show as a preview.
``title``
    The HTML title of the email (not the subject line).
``footer``
    The footer of the email.

Call-to-action (CTA)
--------------------

CTAs can be included via the ``emailpal/really_simple/cta.html`` template.

Here's an example of using the CTA:

.. code-block:: html+django

   {% include "emailpal/really_simple/cta.html" with action="view the site" url="https://example.org" %}

In the HTML version of the email, the above snippet will appear as a large
button with the text "View The Site" on it; clicking the button will
take the user to example.org.

.. highlight:: none

In the plaintext version of the email, the snippet will appear like this::

   To view the site, visit:
   https://example.org

Variables required
::::::::::::::::::

``action``
    The human-readable name of the action the reader is being asked to take, e.g. ``"view the website"``.
``url``
    The URL the user should visit to take the action.

.. _Really Simple Responsive HTML Email Template: https://github.com/leemunroe/responsive-html-email-template
