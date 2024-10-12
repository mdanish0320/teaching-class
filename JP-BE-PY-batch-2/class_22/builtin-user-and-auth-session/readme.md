```python
python3 manage.py migrate
python3 manage.py createsuperuser


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

User.objects.create(
    email="danish@gmail.com", 
    username="danish", 
    password=make_password("admin"),
    is_staff=True,            # Grants access to the admin interface
    is_superuser=True         # Grants all permissions and unrestricted access
)


# Authenticate the user
user = authenticate(request, username=username, password=password)

if user is not None:
    # Log the user in (create session)
    login(request, user)
    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)


if request.user.is_authenticated == False:
    return Response("please login")


logout(request)
```