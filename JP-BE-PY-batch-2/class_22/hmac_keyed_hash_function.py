"""
HMAC involves a secret key, making it a keyed hash function. 
This means that the hash output depends on both the input data and the secret key. 
Without the key, it's computationally infeasible to generate the correct HMAC. 
This adds an extra layer of security, 
especially when you want to ensure that only parties with the secret key can verify the integrity of the message.
"""

import hashlib
import hmac

def generate_hmac(message, key):
    """
    Generate HMAC for a given message and key.
    """
    # Convert the key and message to bytes
    key_bytes = bytes(key, 'utf-8')
    message_bytes = bytes(message, 'utf-8')

    # Use SHA-256 as the hash function
    hash_function = hashlib.sha256

    # Generate the HMAC
    generated_hmac = hmac.new(key_bytes, message_bytes, hash_function).hexdigest()

    return generated_hmac

def validate_hmac(message, key, received_hmac):
    """
    Validate HMAC for a given message, key, and received HMAC.
    """
    # Generate the expected HMAC
    expected_hmac = generate_hmac(message, key)

    # Compare the expected HMAC with the received HMAC
    return hmac.compare_digest(expected_hmac, received_hmac)

# Example usage
message_to_send = "Hello, this is a secret message!"
shared_secret_key = "supersecretkey"

# Sender generates HMAC
hmac_generated = generate_hmac(message_to_send, shared_secret_key)
print(f"Generated HMAC: {hmac_generated}")

# Receiver validates HMAC
is_valid = validate_hmac(message_to_send, shared_secret_key, hmac_generated)
print(f"Is Valid HMAC? {is_valid}")
