import re


def email_parser(email):
    # pattern is generated and compiled below
    email_pattern = re.compile(r'[a-zA-Z][a-zA-Z0-9+]*[a-zA-Z0-9]+@[a-zA-Z][a-zA-Z0-9]+(\.com)$')
    check_email = re.match(email_pattern, email)  # the email is matched against the pattern here

    # check to make sure email entered is of a string, else return None
    if not type(email) is str:
        return None

    if check_email:
        group_email = check_email.group()  # email is grouped here
        split_email = re.split("@", group_email)  # the grouped email is split at the @ here to return a list
        # the list returned is iterated and used to generate a dictionary below.
        record = {"Username": split_email[0],
                  "Domain": split_email[1]
                  }
        return record
    else:
        return "invalid email format"

print(email_parser("+yuhg+t@gmail.net"))


