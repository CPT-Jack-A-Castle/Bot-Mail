import smtplib
import os
from functions import *
# server.set_debuglevel(1) # Décommenter pour activer le debug

print("Welcome to Mysa's Mailing Bot!")

server = smtplib.SMTP('mail server')
server.connect('mail server', port)
print("Connecting...", flush=True)

server.starttls()
server.login('mail', 'password')

print("Connected", flush=True)

expeditor_mail = 'John Doe <john.doe@mail.com>'

# Getting mail subject and body from mail.txt file
subject, body = get_mail("mail.txt")

# Importing the mailing list: change "test_mailing_list.txt"
# to your txt file with the mails
to_addrs = get_mailing_list("test_mailing_list.txt")

# List of files to include
attachment_files = [""]

# Sending mails one by one
for mail in to_addrs:
    print("Sending mail to", mail, flush=True)
    send_mail(expeditor_mail, mail, subject, body, attachment_files, server)

print("All mails were sent")

server.quit()

print("Bye Bye !")
