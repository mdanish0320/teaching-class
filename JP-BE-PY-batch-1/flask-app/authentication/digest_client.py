import requests
from requests.auth import HTTPDigestAuth
url = 'http://localhost:3000'
r = requests.get(url, auth=HTTPDigestAuth('john', 'hello'))

# Digest realm="Authentication Required",nonce="4cfbd235cb1ec756f8cf2693c8943a51",opaque="7e16186fdf339c0e3200fe0bee9aee68",algorithm="MD5",qop="auth

print(r.text)