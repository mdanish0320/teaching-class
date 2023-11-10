# JWTs are encoded, not encrypted, the JSON data you store can be seen by anyone intercepting them
# JWT is signed and not encrypted. everyone can read its contents, but when you don't know the private key, you can't change it.
# if changed anyhow, the signature will not matched

# when we say that the token is digitally signed, we mean that we have created a hash of the data (i.e the user object) using our secret_key and injected the hash into the token.
# on receiving the token back from client, we will again create a hash of the token using our private key and will compare that with receiving token hash.
# then the token will match or not match.

# in the context of JWT (JSON Web Tokens), the public key is typically used to verify the signature, which ensures the integrity and authenticity of the token. The private key is used to sign the token during creation.

import jwt
import rsa


#################################################
SECRET_KEY = "ABCD123"

# create token
token = jwt.encode(
    {"user_id": "123"},
    SECRET_KEY,
    algorithm="HS256"
)
print(token)

# verify token
data=jwt.decode(
    token, 
    SECRET_KEY, 
    algorithms=["HS256"]
)

print(data)
#################################################
# for third party token verification

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

# singed message with private_key
token = jwt.encode(
    {"user_id": "123"},
    private_key_pem,
    algorithm="RS256"
)

print(token)

# verify token
data=jwt.decode(
    token, 
    public_key_pem, 
    algorithms=["RS256"]
)

print(data)

