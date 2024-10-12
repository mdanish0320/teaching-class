import json

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
@permission_classes([AllowAny]) # allow accessing this API publically (without auth)
def signup(request: Request):
  reader_group = Group.objects.get(name="reader")
  data = request.data
  user = User.objects.create(
    username=data['username'],
    password=make_password(data['password']),
    email=data['email'],
  )
  user.groups.add(reader_group)
  return Response("success")

@api_view(['POST'])
@permission_classes([AllowAny]) # allow accessing this API publically (without auth)
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