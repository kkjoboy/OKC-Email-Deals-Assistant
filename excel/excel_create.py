# import excel

FILE_NAME = "../templates/Housing_Template.xlsx"

def main(email_message):
    # Add fields in the template from the calculators
    print("Grabbing calculator fields for excel attachment")

    # Load excel template
    email_message = attach_excel_template(email_message, FILE_NAME)

    # Return excel object for attachment
    return email_message

def attach_excel_template(email_message, filename):
    # Load excel template
    with open(filename, 'rb') as fp:
        # img_data = fp.read()
        # email_message.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

        print("Open file with excel library")
        # Grab template from Housng_Template.xlsx
        # Add attachment to email_message

    # Return excel attached email message
    return email_message