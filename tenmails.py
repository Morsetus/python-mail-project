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


def read_gmail():
    count = 1
    try:
        # Connecting to the mail server
        mail = imaplib.IMAP4_SSL(smtp_server)
        mail.login(from_email,from_pwd)
        mail.select('inbox') # Selected Inbox Folder from server

        # Searching All ids
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0] # Putting searched data to the list

        id_list = mail_ids.split() # Splitting data
        first_email_id = int(id_list[-11]) # Tenth Email
        latest_email_id = int(id_list[-1]) # Newest Email

        # Fetching specific mail
        for i in range(latest_email_id,first_email_id, -1):
            type, data = mail.fetch(str(i), '(RFC822)' )

            # Picking data like Subject, From, payload, content_type from fetched mail
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode())
                    email_subject = msg['subject']
                    email_content = msg.get_payload()
                    email_type = msg.get_content_type()
                    email_from = msg['from']

                    print("------------Mail "+str(count)+"---------------")
                    print ('From : ' + email_from + '\n')
                    print ('Subject : ' + email_subject + '\n')
                      
                    if email_type == 'text/html':
                      print("Can't be shown.")
                    elif email_type == 'text/plain':
                      print (email_content)
                      print(email_type)

                    print("Read full messages from your mail.")
                    print("------------Ending----------------")
                    print(" ")
                    count += 1

    except Exception as e:
        print (str(e))

