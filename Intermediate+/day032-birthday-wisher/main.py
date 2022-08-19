import pandas
import smtplib
import ssl
import datetime as dt
from random import randint

SMTP = "smtp.gmail.com"
PORT = 465
FROM = "kyloyd.python@gmail.com"
TO = "kyloyd.python@yahoo.com"
PASSWORD = "efvwlkqcfdtxiyoi"

birthdays = pandas.read_csv('birthdays.csv').to_dict(orient='records')
now = dt.datetime.now()
try:
    birthday_for_today = [b for b in birthdays if b["month"] == now.month and b["day"] == now.day][0]
except KeyError:
    birthday_for_today = None

if birthday_for_today is None:
    print("No birthdays today!")
    exit()

with open(f"letter_templates/letter_{randint(1,3)}.txt") as template_file:
    template = template_file.read()
    output = template.replace("[NAME]", birthday_for_today["name"])

SSL = ssl.create_default_context()
with smtplib.SMTP_SSL(host=SMTP, port=PORT, context=SSL) as server:
    server.login(FROM, PASSWORD)
    server.sendmail(from_addr=FROM, to_addrs=TO, msg=f"Subject: Happy Birthday!\n\n{output}")
