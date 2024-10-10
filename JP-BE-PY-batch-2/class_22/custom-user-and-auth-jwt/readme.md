Here’s the revised version of your instructions, incorporating your feedback and ensuring clarity:

# Create Custom User Instructions

### Project Structure
Ensure your project structure looks like this initially:

```
project_name/
    manage.py
    main/
        settings.py
    api/
        urls.py
        views.py
```

### Step 1: Create the Custom User Model

1. **Create `models.py`** in `project_name/api` if it doesn’t exist.
2. **Add the following code** to `models.py`:

```python
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
```

### Step 2: Update `settings.py`

1. **Open `settings.py`** located in `project_name/main/`.
2. **Update the `INSTALLED_APPS`** section to include your app:

```python
INSTALLED_APPS = [
    ...
    'api',  # Ensure your app is included
]

# Set the custom user model
AUTH_USER_MODEL = 'api.User'  # Ensure this references your User model correctly
```

### Step 3: Create the Serializer

1. **Create `serializers.py`** inside `project_name/api` if it doesn’t exist.
2. **Add the following code** to `serializers.py`:

```python
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    # Define required fields
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    dob = serializers.DateField(required=True)

    # Read-only fields
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    last_login = serializers.DateField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
```

### Step 4: Update the Views

1. **Open `views.py`** located in `project_name/api/`.
2. **Update the views to handle GET and POST requests** as follows:

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data=data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)  # Use request.data to get the posted data
        if serializer.is_valid():
            user_data = serializer.validated_data
            user_data['is_staff'] = True # to be able to login on admin portal
            user = User(**user_data)
            user.set_password("admin")      # Securely hashes and sets the password
            user.save()
            return Response(UserSerializer(user).data, status=201)  # Return the serialized data of the created user
        return Response(serializer.errors, status=400)  # Return errors if validation fails
```

### Step 5: Configure URLs

1. **Update `urls.py`** in `project_name/api` to include the view:

```python
from django.urls import path
from .views import user_list

urlpatterns = [
    path('users/', user_list, name='user-list'),  # Define the endpoint for users
]
```

### Step 6: Create the Migrations Folder

1. **Under the `api` folder, create a folder named `migrations`.**
2. **Inside the `migrations` folder, create a file named `__init__.py`.**


### step 7: Updated Project Structure
```
project_name/
    manage.py
    main/
        settings.py
    api/
        urls.py
        views.py
        models.py
        serializers.py
        migrations/
            __init__.py
```

### Step 8: Run Migrations

After setting everything up, run the following commands to create and apply migrations for your custom user model:

```bash
python manage.py makemigrations
python manage.py migrate
```

**Alternatively**, if you do not create the `migrations` folder manually, run:

```bash
python manage.py makemigrations api  # This will create migrations for the api app
python manage.py migrate
```

### Step 9: Test Your API

- Use tools like Postman or curl to test the endpoints:
  - **GET** request to `/users/` to list all users.
  - **POST** request to `/users/` to create a new user with JSON data, such as:

```json
{
    "email": "danish@gmail.com",
    "password": "admin",
    "dob": "1994-08-25",
    "first_name": "Danish",
    "last_name": "Khan"
}
```
