Django’s `make_password` function is a utility provided by the `django.contrib.auth.hashers` module to securely hash passwords before storing them in a database. It ensures that the password is hashed using a cryptographically secure algorithm, making it resistant to attacks like brute force, dictionary attacks, and rainbow table attacks.

### Key Features of `make_password`

1. **Hashing Algorithms**: By default, `make_password` uses the PBKDF2 algorithm with SHA256, which is a strong, slow hashing algorithm designed to make brute-force attacks more difficult. Django supports multiple hashing algorithms, but PBKDF2 is the default. Others include Argon2, bcrypt, and SHA1 (for backward compatibility).

2. **Salting**: `make_password` automatically generates a unique random salt for each password. A salt is a random value added to the password before hashing it, making each password hash unique, even if two users have the same password.

3. **Algorithm Agnostic**: The function allows you to specify the hashing algorithm you want to use. Django automatically detects which algorithm was used when verifying the password.

4. **Iterations**: For certain algorithms like PBKDF2, `make_password` uses multiple iterations to hash the password, which makes the process slower and more resistant to brute-force attacks.

### Function Signature

```python
make_password(password, salt=None, hasher='default')
```

- `password`: The plain-text password you want to hash.
- `salt` (optional): A random string added to the password to ensure unique hashes. If not provided, Django will generate a secure random salt.
- `hasher` (optional): The hashing algorithm to use. By default, it uses the algorithm defined by `DEFAULT_HASHING_ALGORITHM` in Django's settings (usually PBKDF2).

### Example Usage

```python
from django.contrib.auth.hashers import make_password

# Example 1: Basic usage (automatically generates a salt and uses the default algorithm)
hashed_password = make_password('mypassword123')

# Example 2: Using a custom salt
hashed_password_with_salt = make_password('mypassword123', salt='my_custom_salt')

# Example 3: Using a different algorithm (e.g., bcrypt)
from django.contrib.auth.hashers import is_password_usable
hashed_password_bcrypt = make_password('mypassword123', hasher='bcrypt')

print(hashed_password)
print(hashed_password_with_salt)
print(hashed_password_bcrypt)
```

### How the Output Looks
When you hash a password using `make_password`, the output will be a string in the following format:

```
algorithm$salt$hash
```

For example, the default PBKDF2 hash might look like this:

```
pbkdf2_sha256$260000$Nz5sxrX1$W+TReHxJZcIw7EyO0Av2g1a+tU4wE0ry2wv/Ptp4N9E=
```

In this example:
- `pbkdf2_sha256` is the algorithm used.
- `Nz5sxrX1` is the randomly generated salt.
- The remaining string is the actual hashed password.

### Why `make_password` is Secure

1. **Random Salt**: Each password gets a unique salt, so even if two users have the same password, their hashes will be different.
2. **Secure Algorithms**: The algorithms provided by Django (PBKDF2, bcrypt, Argon2) are considered highly secure and are designed to be slow to compute, making them resistant to brute-force attacks.
3. **Pluggable Hashing Backends**: You can easily switch to a stronger hashing algorithm in the future without breaking backward compatibility.
4. **Multiple Iterations**: Algorithms like PBKDF2 perform many iterations of hashing to slow down attackers.

### Conclusion

The `make_password` function in Django provides a secure, configurable way to hash passwords before storing them in the database. With its support for strong algorithms, automatic salting, and easy-to-use interface, it’s a highly recommended way to handle password security in Django applications.