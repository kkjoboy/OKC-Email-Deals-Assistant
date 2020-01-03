import smtplib
from email.message import EmailMessage

from ../excel.excel_create import (main as excel_main)

FROM_EMAIL = "joshuamielke@gmail.com"
TO_EMAIL = "joshuamielke@gmail.com"

def main():

    # Create the container email message.
    email_message = EmailMessage()

    email_message['Subject'] = 'OKC Property Test Email' # TODO: Delete this. Replace with address of property.

    email_message['From'] = FROM_EMAIL
    email_message['To'] = TO_EMAIL

    email_message.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    email_message = excel_main(email_message)

    # Send the email via our own SMTP server.
    with smtplib.SMTP('localhost') as s:
        s.send_message(email_message)