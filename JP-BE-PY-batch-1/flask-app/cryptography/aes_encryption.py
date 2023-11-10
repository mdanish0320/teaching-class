# cryptography refers to secure information and communication techniques derived from mathematical concepts

# Cipher Text
# Encryption
# Decryption

from cryptography.fernet import Fernet 
  
def generate_key():
    secret_key = Fernet.generate_key() 
    print(secret_key)

# generate_key()
secret_key = "JrKREl6uxSjmG2Fnz9v5YWq-MGDXVEAqeBZPgJit024="
  
# value of key is assigned to a variable 
f = Fernet(secret_key) 
  
# the plaintext is converted to ciphertext 
token = f.encrypt(b"hello world") 
  
# display the ciphertext 
print(token) 
  
# decrypting the ciphertext 
d = f.decrypt(token) 
  
# display the plaintext 
print(d) 