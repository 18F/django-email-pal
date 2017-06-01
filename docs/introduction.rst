Introduction
============

django-email-pal attempts to solve a number of issues we've
had when iterating on projects at `18F`_.

"What kinds of emails are we sending out?"
------------------------------------------

Throughout the life of a project, designers and content authors
often have a difficult time figuring out what kinds of emails
their project sends out, because they're not easily discoverable
or well-documented.

django-email-pal attempts to solve this by providing a built-in
"example email gallery" that showcases example versions of every
kind of email that can be sent out, in both HTML and plaintext
formats, with accompanying documentation.

This gallery also makes it very easy to *iterate* on the content and
design of an email: instead of constantly sending oneself
an email through the app, a designer can just make changes to
a template and see the immediate effects in their browser, iterating
on it just as they'd do with any other Django view.

"Wait, we have to write our email's HTML like it's 1995?"
---------------------------------------------------------

Simply getting started with HTML email can be daunting due to
the lack of standards and wide variety of email clients one must
support. It should be easy to send HTML emails that look nice,
without having to figure out a bunch of arcane tricks to ensure
they don't break on popular email clients.

Solutions to this problem are varied. django-email-pal gives you
the freedom to choose your own HTML email framework if you need to,
but it also comes with a nice solution out-of-the-box: Lee Munroe's
`Really Simple Responsive HTML Email Template`_.

"There are people who can't read HTML email?"
---------------------------------------------

Email is often designed in HTML form first, with the plaintext
alternative left as an afterthought.

Some projects just strip the HTML tags to generate the plaintext.
However, this doesn't always result in an intelligible email, as
there may have been buttons or hyperlinked phrases in the original HTML
version that no longer make much sense.

Other projects have completely separate HTML and plaintext versions
that are specified independently of one another. Yet this is
cumbersome too, as both versions are *mostly* identical and can
easily get out of sync.

django-email-pal attempts to solve this by providing a simple two-pass
template rendering strategy that allows both the HTML and plaintext
versions of an email to be generated from the same template. This
allows *most* of the content to be reused, but also allows for minor 
modifications based on the email's content type.

.. _18F: https://18f.gsa.gov/
.. _Really Simple Responsive HTML Email Template: https://github.com/leemunroe/responsive-html-email-template
