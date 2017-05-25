from mypy_extensions import TypedDict

from .. import VERSION, SendableEmail

def test_version_is_a_string():
    assert type(VERSION) is str


MyContext = TypedDict('MyContext', {'full_name': str})

class MySendableEmail(SendableEmail[MyContext]):
    template_name = 'my_sendable_email.html'
    subject = 'howdy {full_name}!'


def test_sending_email_works():
    ctx = MyContext(full_name='boop jones')
    e = MySendableEmail()

    assert e.render_subject(ctx) == 'howdy boop jones!'

    html = e.render_body_as_html(ctx)
    text = e.render_body_as_plaintext(ctx)

    assert "Hello boop jones" in html
    assert "Hello boop jones" in text

    assert "I am plaintext" in text
    assert "I am not HTML" in text

    assert "I am HTML" in html
    assert "I am <strong>not</strong> plaintext" in html

    e.send_messages(ctx)
