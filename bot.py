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
attachment_files = []

size = len(to_addrs) # Mailing list size
i = 0
pas = 100 # Number of mails to send at the same time

while (i + pas) < size:
    l = to_addrs[i:(i+pas)]
    print("Sending mail to", len(l), "persons", flush=True)
    send_mail(expeditor_mail, l, subject, body, attachment_files, server)
    i += pas

l = to_addrs[i:]
print("Sending mail to", len(l), "persons", flush=True)
send_mail(expeditor_mail, l, subject, body, attachment_files, server)

print("All mails were sent")

server.quit()

print("Bye Bye !")
