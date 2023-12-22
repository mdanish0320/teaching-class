from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import UserSerializer

# it will not hash the password
class Usermvs(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# use  User.objects.create()
class Usermvs_2(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request: Request, *args, **kwargs):
        data = request.data
        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            username=data['username'],
        )
        user.set_password("admin")
        user.save()
        
        # Create a serializer instance for the created user
        serializer = UserSerializer(user)

        # Return serialized data
        return Response(serializer.data)
    

# use  serializer.save()
class Usermvs_3(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password("admin")
            user.save()

            # Return serialized data
            return Response(serializer.data)
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)
