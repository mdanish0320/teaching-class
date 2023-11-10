import rsa

def generate_rsa_keys():
    # generate public and private keys with 
    # rsa.newkeys method,this method accepts 
    # key length as its parameter
    # key length should be atleast 16
    public_key, private_key = rsa.newkeys(512)
    
    # Convert keys to PEM format
    public_key_pem = public_key.save_pkcs1().decode('utf-8')
    private_key_pem = private_key.save_pkcs1().decode('utf-8')

    print(public_key_pem)
    print(private_key_pem)
    return public_key_pem, private_key_pem


# generate_rsa_keys()

public_key_pem = """-----BEGIN RSA PUBLIC KEY-----
MEgCQQCKZODGlbJwj1SnW6d23zkmJD0mTB2iN9RxPBTOz+m0w9jj2RsohTvTWWhV
6mbC/ujKn9GRDoSOMHx8GTUuSdzpAgMBAAE=
-----END RSA PUBLIC KEY-----
"""
private_key_pem ="""-----BEGIN RSA PRIVATE KEY-----
MIIBOwIBAAJBAIpk4MaVsnCPVKdbp3bfOSYkPSZMHaI31HE8FM7P6bTD2OPZGyiF
O9NZaFXqZsL+6Mqf0ZEOhI4wfHwZNS5J3OkCAwEAAQJAY9Lv7037MAWy4iTSXoQV
DNYG5aDxnxj2O9dCiwqc143exiYML2JkZkxfh/S+KUl17FVAC5AfJpJA0K9wDkzu
oQIjAL4bt4GSfi80FYbCn4jqlTny5Qll32xtjLffZ4T62dDn6LsCHwC6XJC9veKd
bLbhi58Zy7/HjCeS6qFpLFgee5whuKsCIiV+F+HQ/1vV3Mz4Azigcw+7rJn+4mJi
9Jaq06KxSlXd9tMCHh/MF24obfgKSpHlLrpKB2jWwxHQMsYtKMPat2MRjQIiFyJn
CbMUZ+vw0dwqREX/RoCy4CisN8pT0dzjGYav0qJmjA==
-----END RSA PRIVATE KEY-----
"""

# Example message
message = "Hello, this is a secret message!"

# Encrypt message using the public key
enc_message = rsa.encrypt(message.encode(), rsa.PublicKey.load_pkcs1(public_key_pem))


print("original string: ", message)
print("encrypted string: ", enc_message)

# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(enc_message, rsa.PrivateKey.load_pkcs1(private_key_pem)).decode()

print("decrypted string: ", decMessage)