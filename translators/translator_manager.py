from .table_translator import (main as table_main)
from .spearhead_translator import (main as spearhead_main)
from .translator_utils import (parse_email_in_brackets, parse_name_from_email)

TABLE_EMAILS = ["hello@table.investments"]
SPEARHEAD_EMAILS = ["OKC@southcentralmatrixmail.com"]

# Take email list as parameter
def main(email_list):

    # Check whether any of the emails fit from addresses defined by the translators
    # Parse out the emails that fit a translator into different lists
    parsed_email_list = parse_email_list(email_list)

    # print("Parsed email list: ")
    # print(parsed_email_list)
    # print()

    # Create list of parameters to send to calculator
    parameter_list = []

    # For each list of emails, choose translator
    for email_list in parsed_email_list:

        for email_message in email_list:

            # Call translator on each email
            if email_list == parsed_email_list[0]: # Table Investments
                table_parameters = table_main(email_message)
                parameter_list.append(table_parameters)

            elif email_list == parsed_email_list[1]: # Spearhead Realty
                spearhead_parameters = spearhead_main(email_message)
                parameter_list.append(spearhead_parameters)

    return parameter_list

# Check whether any of the emails fit from addresses defined by the translators
# Parse out the emails that fit a translator into different lists
def parse_email_list(email_list):

    parsed_email_list = []
    table_list = []
    spearhead_list = []

    for email_message in email_list:
        # print("Email Message subject: " + email_message.get("Subject"))
        # print("Email Message from: " + email_message.get("From"))
        # print("Email Message to: " + email_message.get("To"))

        if parse_email_from(email_message)[1] in TABLE_EMAILS:
            table_list.append(email_message)
            print("Adding email to table_list from: " + email_message.get("From"))

        if parse_email_from(email_message)[1] in SPEARHEAD_EMAILS:
            spearhead_list.append(email_message)
            print("Adding email to spearhead_list from: " + email_message.get("From"))
    
        print()

    parsed_email_list.append(table_list)
    parsed_email_list.append(spearhead_list)
    
    return parsed_email_list

def parse_email_from(email_message):
    # Get the from field from the email headers
    email_from = email_message.get("From")

    # Split from component into two
    # Email is everything in the <>
    email = parse_email_in_brackets(email_from)
    
    # Name is everything else minus edge whitespace and <>
    name = parse_name_from_email(email_from)

    # if name != None:
    #     print("Email from name: " + name)
    # else:
    #     print("Email from name: None")
    # print("Email from email: " + email)

    return name, email