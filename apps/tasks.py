import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from root.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT


def send_mail(receiver_email , code):

    sender_email = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verify code"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""Code : {code}"""

    part1 = MIMEText(text, "plain")
    message.attach(part1)
    with smtplib.SMTP_SSL(EMAIL_HOST, 465) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )