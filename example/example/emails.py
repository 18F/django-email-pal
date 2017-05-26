from typing import Dict, Any  # NOQA
from emailpal import SendableEmail


class MySendableEmail(SendableEmail):
    """
    This is a simple example email.
    """

    template_name = 'emailpal/my-template.html'
    subject = 'hello'
    example_ctx = {}  # type: Dict[str, Any]
