from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated

# from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserRegisterSerializer, AdminRegisterSerializer

# Create your views here.
class RegisterUser(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
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
