from django.http import Http404
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.template.response import TemplateResponse


def example_view(request, template_name, is_html_email):
    context = dict(is_html_email=is_html_email)
    try:
        template = get_template('emailpal/{0}.html'.format(template_name))
    except TemplateDoesNotExist:
        raise Http404("No such template")
    # we'll call the html-stripping code, etc. here
    return TemplateResponse(request, template, context,
                            'text/html' if is_html_email else 'text/plain')
