import traceback
import os
import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from typing import List

def send_mail(send_from: str,
                send_to: List[str],
                subject: str,
                text: str,
                files=[],
                server="127.0.0.1"
            ):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        with open(f, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=os.path.basename(f)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
        msg.attach(part)

    try:
        smtp = smtplib.SMTP(server)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
    except smtplib.SMTPException:
        print("Error: unable to send email")
    except ValueError:
        print("Error: invalid port")
    except:
        print("Error: unknown error")
        traceback.print_exc()

send_mail(
    send_from = input("Sender: "),
    receivers = input("Receivers (separate with spaces): ").split(),
    subject = input("Subject: "),
    text = input("Body: "),
    files = input("Files (separate with spaces): ").split(),
)