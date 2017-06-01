import abc
import re
from typing import Dict, TypeVar, Generic, Dict, Any, cast  # NOQA
from django.utils.safestring import SafeString
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

T = TypeVar('T')


def collapse_and_strip_tags(text: str) -> str:
    '''
    Strips HTML tags and collapases newlines in the given string.

    Example:

      >>> collapse_and_strip_tags('\\n\\n<p>hi james</p>\\n\\n\\n')
      '\\nhi james\\n'
    '''

    return re.sub(r'\n+', '\n', strip_tags(text))


class SendableEmail(Generic[T], metaclass=abc.ABCMeta):
    '''
    This abstract base class represents a template-based email that can
    be sent in HTML and plaintext formats.
    '''

    @property
    @abc.abstractmethod
    def example_ctx(self) -> T:
        '''
        An example context with which the email can be rendered.
        '''

        pass  # pragma: no cover

    @property
    @abc.abstractmethod
    def subject(self) -> str:
        '''
        The subject line of the email. This is processed by
        :py:meth:`str.format` and passed the same context that is
        passed to templates when rendering the email, so you can
        include context variables via brace notation, e.g.
        ``Hello {full_name}!``.
        '''

        pass  # pragma: no cover

    @property
    @abc.abstractmethod
    def template_name(self) -> str:
        '''
        The path to the template used to render the email, e.g.
        ``my_app/my_email.html``.

        Aside from the context your code provides, the following
        context variables are also defined:

        * ``is_html_email`` is ``True`` if (and only if) the
          template is being used to render the email's HTML representation.

        * ``is_plaintext_email`` is ``True`` if (and only if) the
          template is being used to render the email's plaintext
          representation.

        Note that when rendering the email as plaintext, HTML tags
        are automatically stripped from the generated content.
        '''

        pass  # pragma: no cover

    def _cast_to_dict(self, ctx: T) -> Dict[str, Any]:
        if not isinstance(ctx, dict):
            raise ValueError('context must be a dict subclass')
        return cast(Dict[str, Any], ctx)

    def render_body_as_plaintext(self, ctx: T) -> str:
        plaintext_ctx = self._cast_to_dict(ctx).copy()
        plaintext_ctx['is_html_email'] = False
        plaintext_ctx['is_plaintext_email'] = True

        return collapse_and_strip_tags(
            render_to_string(self.template_name, plaintext_ctx)
        )

    def render_body_as_html(self, ctx: T) -> SafeString:
        html_ctx = self._cast_to_dict(ctx).copy()
        html_ctx['is_html_email'] = True
        html_ctx['is_plaintext_email'] = False
        body = render_to_string(self.template_name, html_ctx)

        # TODO: This is a workaround for
        # https://github.com/18F/calc/issues/1409, need to figure
        # out the exact reason behind it.
        body = body.encode('ascii', 'xmlcharrefreplace').decode('ascii')

        return SafeString(body)

    def render_subject(self, ctx: T) -> str:
        return self.subject.format(**self._cast_to_dict(ctx))

    def send_messages(self, ctx: T, from_email=None, to=None, bcc=None,
                      connection=None, attachments=None, headers=None,
                      alternatives=None, cc=None, reply_to=None) -> int:
        '''
        Renders the email using context specified by ``ctx`` and sends it.

        Aside from ``ctx``, arguments to this method are the
        same as those for :py:class:`django.core.mail.EmailMessage`.
        '''

        msg = EmailMultiAlternatives(
            subject=self.render_subject(ctx),
            body=self.render_body_as_plaintext(ctx),
            from_email=from_email,
            to=to,
            bcc=bcc,
            connection=connection,
            attachments=attachments,
            headers=headers,
            alternatives=alternatives,
            cc=cc,
            reply_to=reply_to,
        )
        msg.attach_alternative(self.render_body_as_html(ctx), 'text/html')
        return msg.send(fail_silently=False)
