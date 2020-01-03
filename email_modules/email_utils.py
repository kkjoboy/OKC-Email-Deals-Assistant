import imaplib
import time

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "joshuamielke" + ORG_EMAIL
FROM_PWD    = "igluqlbdkiprideo"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
MAILBOX =  "inbox"


def mail_login():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
        print("Attempting to login to email address " + FROM_EMAIL + ".")
        mail.login(FROM_EMAIL,FROM_PWD)
        print("Successfully logged in to email address " + FROM_EMAIL + ".\n")

        mail.select(MAILBOX) # Select email inbox
    except Exception:
        print("Exception encountered in mail_login().")
        raise

    return mail

def mail_logout(mail):
    mail.close()
    mail.logout()