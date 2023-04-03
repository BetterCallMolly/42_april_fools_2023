import traceback
import os
import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from typing import List

from dotenv import load_dotenv

load_dotenv()

def send_mail(send_from: str,
                send_to: List[str],
                subject: str,
                text: str,
                server: str,
                port: int,
                password: str,
                files=[],
            ):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    smtp_server = smtplib.SMTP_SSL(server, port)
    smtp_server.login(send_from, password)

    for f in files:
        with open(f, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=os.path.basename(f)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
        msg.attach(part)

    try:
        smtp_server.sendmail(send_from, send_to, msg.as_string())
        smtp_server.close()
    except smtplib.SMTPException:
        print("Error: unable to send email")
    except ValueError:
        print("Error: invalid port")
    except:
        print("Error: unknown error")
        traceback.print_exc()
try:
    send_mail(
        send_from = os.environ["send_from"],
        send_to = os.environ["send_to"].split(","),
        subject = os.environ["subject"],
        text = os.environ["text"],
        server = os.environ["server"],
        port = int(os.environ["port"]),
        files = os.environ["files"].split(","), 
        password = os.environ["password"],
    )
except KeyError:
    print(".env not properly set")
except ValueError:
    print(".env contains an invalid port")
