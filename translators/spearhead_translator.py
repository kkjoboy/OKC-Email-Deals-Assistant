import email

def main(email_message):
    print("Entered spearhead_main().\n")

    # Parse email message into message body
    for part in email_message.walk():
        print(part.get_content_type())

    print(email_message.get_payload())

    print(email.version)

    # Return address components, price, etc
    return 0