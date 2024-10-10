import json

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

@api_view(['GET', 'POST'])
def create_or_get_users(request: Request):
    if request.method == 'GET':
        data = User.objects.all()
        users = []
        for user in data:
            users.append({
                "email": user.email,
                "username": user.username,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser
            })
    
    if request.method == 'POST':
        # User can login and act as an administrator with full control
        User.objects.create(
            email="danish@gmail.com", 
            username="danish", 
            password=make_password("admin"),
            is_staff=True,            # Grants access to the admin interface
            is_superuser=True         # Grants all permissions and unrestricted access
        )


        # User can only login to the admin, but can only perform actions they have specific permissions for
        user = User(
            email="fahad@gmail.com", 
            username="fahad",
            is_staff=True              # Grants access to the admin interface, but permissions are needed for specific actions
        )
        user.set_password("admin")      # Securely hashes and sets the password
        user.save()



        # Improper configuration: This user cannot log in to the admin because 'is_staff' is missing
        User.objects.create(
            email="shoaib@gmail.com", 
            username="shoaib", 
            password=make_password("admin"),
            is_superuser=True          # Grants all permissions, but without 'is_staff', they cannot log in
        )
        
        users = "success"

    return Response(users, status=status.HTTP_200_OK)



@api_view(['GET'])
def create_or_get_posts(request: Request):
    if request.user.is_authenticated == False:
        return Response("please login")
    
    data = {
        "is_authenticated": request.user.is_authenticated,
        "is_staff": request.user.is_staff,
        "is_superuser": request.user.is_superuser,
        "email": request.user.email,
    }
    return Response(data)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Log the user in (create session)
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def logout_view(request):
    # Log the user out (destroy session)
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


"""
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
"""