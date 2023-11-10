import bcrypt 

# example password 
password = 'password123'

# converting password to array of bytes 
bytes = password.encode('utf-8') 

# generating the salt 
salt_byte = bcrypt.gensalt(12) 
print("salt:", salt_byte)
# salt = "$2b$12$IW7OZzl4nkLafX9VStwSWe"
# salt_byte = salt.encode('utf-8') 

# Hashing the password 
hash = bcrypt.hashpw(bytes, salt_byte) 

print("hashed_password:", hash)

salt = hash[7:29]
hash_part = hash[29:]

print("salt:", salt)
print("hash", hash_part)



"""
#$2a$[cost]$[22 characters of salt][31 characters of hash]

$2a$: This indicates the bcrypt algorithm version.
[cost]: This represents the cost factor used during hashing. It's a logarithmic factor that determines the number of iterations (higher values mean more iterations).
[22 characters of salt]: The randomly generated salt, encoded in the hash.
[31 characters of hash]: The resulting hash.
"""
