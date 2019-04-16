import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def attach_file(message, attachment_file):
    # Open PDF file in binary mode
    with open(attachment_file, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_file}",
    )
    message.attach(part)

    return message

def send_mail(expeditor_mail, destination_mail, subject, body, attachment_files, server):
    message = MIMEMultipart()
    message['From'] = expeditor_mail
    message['To'] = destination_mail
    message['Subject'] = subject
    message.attach(MIMEText(body, "plain"))

    for file in attachment_files:
        message = attach_file(message, file)

    text = message.as_string()

    server.sendmail(expeditor_mail, destination_mail, text)

def get_mail(filename):
    file = open(filename, "r", encoding='UTF-8')
    subject = file.readline()
    file.readline()
    body = ""
    for line in file.readlines():
        body += line
    file.close()
    return (subject, body)

def get_mailing_list(filename):
    file = open(filename, "r")
    lines = file.readlines()
    to_addrs = []
    for line in lines:
        to_addrs.append(line)
    file.close()
    return to_addrs
