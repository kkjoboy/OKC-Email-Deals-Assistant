import time
import email
import sys

from .email_utils import (mail_login, mail_logout)

print("Python Version: " + sys.version + "\n")

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "joshuamielke" + ORG_EMAIL
MAILBOX =  "inbox"

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def get_mail_list(mail):

    # search mail in the selected mailbox
    try:
        print("Retreiving list of emails from: " + MAILBOX + ".")

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        print("Successfully retrieved emails from: " + MAILBOX + ".\n")

    except Exception:
        print("Exception encountered in get_mail_list().")
        raise

    return id_list

def get_email_list():

    try:
        # login to email
        mail = mail_login()
        print("Logged into the email at: " + FROM_EMAIL)

        # get email list
        id_list = get_mail_list(mail)
        print("Retrieved email list.")

        # print("Email List: ")
        # print(id_list)
        # print()

        email_list = []

        for num in id_list:
            status, data = mail.fetch(num, '(RFC822)')
            msg = data[0][1]
            email_message = email.message_from_bytes(msg)

            if status == "OK":
                email_list.append(email_message)
            else:
                print("Status returned " + status + ".")

            # print("Is the email message a multipart?: " + str(email_message.is_multipart()))

            # print("Status is: " + status)
            # print("Status type is: " + str(type(status)))
            
            # print("Email Message: ")
            # print(email_message)

            # print("Email Message Payload: ")
            # print(email_message)

            # print("Email Message Keys: ")
            # print(email_message.keys())

            # print("Email Message Values: ")
            # print(email_message.values())

            # print("Email Message subject: " + email_message.get("Subject"))

            # print("Email Message from: " + email_message.get("From"))

            # print("Email Message to: " + email_message.get("To"))

            # print()

        mail_logout(mail)

    except Exception:
        print("Exception encountered in choose_translator().")
        raise

    return email_list

def main():
    print("Email Reader Started.")
    email_list = get_email_list()
    print("Email Reader returned email list.")

    return email_list