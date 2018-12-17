# -*- coding: cp1252 -*-

import smtplib
import time
import imaplib
import email
import creds

# Fetching credentials
from_email  = creds.from_email
from_pwd    = creds.from_pwd
smtp_server = creds.smtp_server
smtp_port   = creds.smtp_port


def show_unseen():
    try:
        # Connecting to the mail server
        mail = imaplib.IMAP4_SSL(smtp_server)
        mail.login(from_email,from_pwd)
        mail.select('inbox') # Selected Inbox Folder from server

        # Searching UNSEEN mail ids
        type, data = mail.search(None, 'UNSEEN')
        mail_ids = data[0] # Putting searched data to the list

        id_list = mail_ids.split() # Splitting data
        id_list = len(id_list) # Formating to len() for future use
        return id_list 
       
    except Exception as e:
        print (str(e))

# Todo: read_unseen()
def read_unseen():
    try:
        mail = imaplib.IMAP4_SSL(smtp_server)
        mail.login(from_email,from_pwd)
        mail.select('inbox')

        type, data = mail.search(None, 'UNSEEN')
        count = len(data[0].split())
        print(count)


       
    except Exception as e:
        print (str(e))