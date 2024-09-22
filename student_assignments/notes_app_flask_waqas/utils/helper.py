import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8') 
    hash = bcrypt.hashpw(bytes,salt)
    return hash

def check_missing_fields(fields,body):
    missing_fields =[]
    for field in fields:
        if not body.get(field):
            missing_fields.append(field)
    return missing_fields        
    # pass