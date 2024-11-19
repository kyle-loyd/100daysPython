import smtplib
from ssl import create_default_context

SMTP = "smtp.gmail.com"
PORT = 465
FROM = "kyloyd.python@gmail.com"
TO = "kyloyd.python@yahoo.com"
PASSWORD = "REDACTED"


def send():
    ssl = create_default_context()
    with smtplib.SMTP_SSL(host=SMTP, port=PORT, context=ssl) as server:
        server.login(FROM, PASSWORD)
        server.sendmail(from_addr=FROM, to_addrs=TO, msg=f"The ISS may be visible!")
