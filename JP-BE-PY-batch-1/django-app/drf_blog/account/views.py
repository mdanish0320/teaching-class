from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, AdminRegisterSerializer

# Create your views here.
class RegisterUser(APIView):
    serializer = UserRegisterSerializer
    def post(self, request):
        serialized_user = self.serializer(data=request.data)
        if serialized_user.is_valid(raise_exception=True):
            serialized_user.save()
            return Response({"message": "blogger user created"})


class RegisterAdmin(APIView):
    serializer = AdminRegisterSerializer
    def post(self, request):
        serialized_user = self.serializer(data=request.data)
        if serialized_user.is_valid(raise_exception=True):
            serialized_user.save()
            return Response({"message": "admin user success"})


class LoginUser(APIView):
    def post(self, request):
        print("register user", request.data)
        return Response({"message": "login success"})