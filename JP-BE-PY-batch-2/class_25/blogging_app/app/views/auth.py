import json

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from ..serializers import LoginSerializer, SignupSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["GET", "POST"])
def signup_view(request: Request):

    if request.method == "POST":
        serializer = SignupSerializer(data=request.query_params)
        if serializer.is_valid():
            # User can login and act as an administrator with full control
            User.objects.create(
                username=serializer.validated_data["username"],
                password=make_password(serializer.validated_data["password"]),
                is_staff=True,  # Grants access to the admin interface
            )
        else:
            return Response(
                serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
            )

    return Response("signup successful", status=status.HTTP_200_OK)


@api_view(["POST"])
def login_view(request: Request):
    data = request.data  # json input from user
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data

        user = authenticate(
            request, username=data["username"], password=data["password"]
        )
        if user is not None:
            # login(request, user)
            refresh_token = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh_token": str(refresh_token),  # expiry 30 days
                    "access_token": str(refresh_token.access_token),  # expiry 1 day
                }
            )
        else:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
