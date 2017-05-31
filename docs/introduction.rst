Introduction
============

Throughout the life of a project, designers and content authors
often have a difficult time figuring out what kinds of emails
their projects send out, because they're not easily discoverable
or well-documented.

Furthermore, email is often designed in HTML form first, with
the plaintext alternative left as an afterthought. Just
stripping the HTML tags to generate the plaintext doesn't always
result in an intelligible email, as there may be buttons or
hyperlinked phrases in the original HTML version that don't make
much sense as plaintext. Yet it also doesn't make sense to
require both content types to be specified completely independently
of one another, as they *do* contain most of the same content.

Lastly, simply getting started with HTML email can be daunting due to
the lack of standards and wide variety of email clients one must
support.

django-email-pal attempts to solve these problems by:

* Providing a built-in "example email gallery" endpoint that
  showcases example versions of every kind of email that can
  be sent out, in both HTML and plaintext formats, with documentation;

* Providing a simple two-pass template rendering strategy that allows
  both the HTML and plaintext versions of an email to be generated
  from the same template, thus allowing *most* of the content to be
  reused but allowing for minor modifications based on the content
  type;

* Making it easy to add email rendering to the project's test suite,
  ensuring that they behave as expected and don't crash the server.

* Making it easy to get started with sending lightweight
  HTML emails that look nice across a wide variety of email clients by 
  allowing developers to optionally leverage Lee Munroe's
  `Really Simple Responsive HTML Email Template <reallysimple_>`_.

.. _reallysimple: https://github.com/leemunroe/responsive-html-email-template
