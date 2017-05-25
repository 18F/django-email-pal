Base Template Documentation
===========================

Variables Used
--------------
``is_html_email``
    ``True`` is the content is HTML, ``False`` otherwise.


Blocks Defined
--------------
These can be overridden by templates that inherit from the base.

``content``
    The content for the email.

    Example content can be found at https://github.com/leemunroe/responsive-html-email-template/blob/c12462fe223858f4d8bf9265453f7f1776640976/email.html#L289-L307
``preheader``
    The contents of a ``<span>`` with a ``class`` of ``preheader``, which some email clients will show as a preview.
``title``
    The HTML title of the email (not the subject line).
