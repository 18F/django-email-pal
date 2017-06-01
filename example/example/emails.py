from emailpal import SendableEmail


class MySendableEmail(SendableEmail):
    """
    This is a simple example email.
    """

    template_name = 'example/my_template.html'
    subject = 'Check this out, {full_name}!'
    example_ctx = {'full_name': 'Jane Doe'}
