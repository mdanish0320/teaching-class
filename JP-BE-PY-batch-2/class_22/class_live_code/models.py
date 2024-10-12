from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Remove username by setting it to None
    username = None

    # Make email the unique identifier
    email = models.EmailField(unique=True)

    # Set USERNAME_FIELD to email
    USERNAME_FIELD = 'email'
    
    # Required fields for creating a superuser
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Optionally, you can add other fields like user type, etc.
    dob = models.DateField()

    def __str__(self):
        return self.email