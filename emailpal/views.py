from django.http import Http404, HttpResponse
from django.urls import reverse
from django.template.response import TemplateResponse

from .apps import get_sendable_emails


def example_view(request, name, is_html_email):
    sendable_email = get_sendable_emails().get(name)
    if sendable_email is None:
        raise Http404("No such email")
    email = sendable_email()
    if is_html_email:
        content_type = 'text/html'
        content = email.render_body_as_html(email.example_ctx)
    else:
        content_type = 'text/plain'
        content = email.render_body_as_plaintext(email.example_ctx)
    return HttpResponse(content, content_type)


def example_index(request):
    examples = []
    for name, sendable_email in get_sendable_emails().items():
        examples.append({
            'name': name,
            'description': sendable_email.__doc__,
            'html_url': reverse('emailpal:example_view_html',
                                kwargs={'name': name}),
            'txt_url': reverse('emailpal:example_view_txt',
                               kwargs={'name': name}),
        })
    return TemplateResponse(request, 'emailpal/index.html', {
        'examples': examples,
    })
