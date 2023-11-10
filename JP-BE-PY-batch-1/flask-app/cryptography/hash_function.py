# hashing is an irreversible process i.e. conversion should be only one way
# the length of hash should be fixed
# an input string should uniquely correspond with a hash so that we can compare them later, this makes it ideal for passwords and authentication.

from hashlib import sha256

txt = "look at me!"
print(sha256(txt.encode('utf-8')).hexdigest())