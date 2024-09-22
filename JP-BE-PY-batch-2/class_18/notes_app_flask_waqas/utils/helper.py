import re

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email(email):
    if re.match(email_regex, email):
        return True
    else:
        return False

def check_missing_fields(fields,body):
    missing_fields =[]
    for field in fields:
        if not body.get(field):
            missing_fields.append(field)
    return missing_fields        
    # pass