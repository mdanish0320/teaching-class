# views.py
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate


from .serializers import UserSerializer, LoginSerializer, SignupSerializer


@api_view(["POST"])
def signup_view(request: Request):
    data = request.data  # json input from user
    serializer = SignupSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        data["password"] = make_password(data["password"])
        User.objects.create(**data)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    return Response("success")


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
            login(request, user)

            # resp = make_response("success")
            # resp.set_cookie(session_id, str(user_id), expire_at=1000, http_only=True)
            return Response("success")
        else:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def logout_view(request: Request):

    logout(request)
    return Response("success")


@api_view(["GET"])
def profile_view(request: Request):
    if request.user.is_authenticated:
        user = UserSerializer(request.user)
        return Response(user.data)
    else:
        return Response("please login")
