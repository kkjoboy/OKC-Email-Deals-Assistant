import re

def parse_email_in_brackets(string):

    parsed_string = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", string)

    return parsed_string.group(0)

def parse_name_from_email(string):

    parsed_string = re.search(r"([^\n]+)<", string)

    if parsed_string == None:
        return None

    parsed_string = parsed_string.group(0)[:-1] # Take off last character (angle bracket)

    parsed_string = parsed_string.strip()

    return parsed_string
